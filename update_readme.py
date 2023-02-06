from datetime import timezone
import re
import pathlib
import sys

import git


root_path = pathlib.Path(__file__).parent.resolve()

index_pattern = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_pattern = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

count_template = "<!-- count starts -->{}<!-- count ends -->"


def get_file_created_and_updated_times(repo_path, ref="main"):
    file_times = {}
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = list(repo.iter_commits(ref))[::-1]
    for commit in commits:
        commit_time = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for file_path in affected_files:
            if file_path not in file_times:
                file_times[file_path] = {
                    "created": commit_time.isoformat(),
                    "created_utc": commit_time.astimezone(timezone.utc).isoformat(),
                }
            file_times[file_path].update(
                {
                    "updated": commit_time.isoformat(),
                    "updated_utc": commit_time.astimezone(timezone.utc).isoformat(),
                }
            )
    return file_times


def regenerate_readme(repo_path):
    file_times = get_file_created_and_updated_times(repo_path)

    index = ["<!-- index starts -->"]

    for folder in root_path.glob("*/"):
        if not folder.is_dir() or folder.stem.startswith("."):
            continue

        folder_path = str(folder.relative_to(root_path))
        topic = folder_path.split("/", maxsplit=1)[0]

        index.append(f"## {topic}\n")

        for file_path in root_path.glob(f"{topic}/*.md"):
            file_url = f"https://github.com/Azanul/til/blob/main/{file_path}"

            with file_path.open() as f:
                title = f.readline().lstrip("#").strip()
                date = file_times[str(file_path.relative_to(root_path))]["created_utc"].split("T")[0]

            index.append(f"* [{title}]({file_url}) - {date}")

    index.append("<!-- index ends -->")
    readme = root_path / "README.md"
    index_txt = "\n".join(index).strip()
    readme_contents = readme.open().read()
    rewritten = index_pattern.sub(index_txt, readme_contents)
    if "--rewrite" in sys.argv:
        readme.open("w").write(rewritten)
    else:
        print(index_txt)


if __name__ == "__main__":
    regenerate_readme(root_path)
