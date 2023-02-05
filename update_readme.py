from datetime import timezone

import pathlib
import sys
import re
import os

import git

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_re = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

COUNT_TEMPLATE = "<!-- count starts -->{}<!-- count ends -->"


def created_changed_times(repo_path, ref="main"):
    times = {}
    print(pathlib.Path(__file__))
    print(repo_path)
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        dt = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for filepath in affected_files:
            if filepath not in times:
                times[filepath] = {
                    "created": dt.isoformat(),
                    "created_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            times[filepath].update(
                {
                    "updated": dt.isoformat(),
                    "updated_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            )
    return times


def recreate_readme(repo_path):
    all_times = created_changed_times(repo_path)

    index = ["<!-- index starts -->"]

    for folder in root.glob("*/"):
        if not folder.is_dir() or folder.stem.startswith("."):
            continue

        path = str(folder.relative_to(root))
        topic = path.split("/", maxsplit=1)[0]

        index.append(f"## {topic}\n")

        for filepath in root.glob(f"{topic}/*.md"):
            url = f"https://github.com/Azanul/til/blob/main/{path}"

            fp = filepath.open()
            title = fp.readline().lstrip("#").strip()
            date = all_times[str(filepath.relative_to(root))]["created_utc"].split("T")[0]

            index.append(
                f"* [{title}]({url}) - {date}"
            )


        # # Do we need to render the markdown?
        # path_slug = path.replace("/", "_")

    index.append("<!-- index ends -->")

    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        rewritten = index_re.sub(index_txt, readme_contents)
        readme.open("w").write(rewritten)
    else:
        print("\n".join(index))


if __name__ == "__main__":
    recreate_readme(root)
