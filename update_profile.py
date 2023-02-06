from datetime import timezone
import re
import pathlib
import sys

import git


root_path = pathlib.Path(__file__).parent.parent.resolve()
til_path = root_path / 'main'
profile_path = root_path / 'Azanul'

blogs_pattern = re.compile(r"<!\-\- blogs starts \-\->.*<!\-\- blogs ends \-\->", re.DOTALL)
tils_pattern = re.compile(r"<!\-\- tils starts \-\->.*<!\-\- tils ends \-\->", re.DOTALL)

count_template = "<!-- count starts -->{}<!-- count ends -->"


def get_file_created_and_updated_times(ref="main"):
    file_times = {}
    repo = git.Repo(til_path, odbt=git.GitDB)
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


def update_tils(repo_path):
    file_times = get_file_created_and_updated_times()

    tils = ["<!-- tils starts -->"]
    print(til_path)

    for file in til_path.glob("*/*.md"):
        print(file, file.is_dir(), file.stem.startswith("."))
        if file.stem.startswith("."):
            continue

        file_path = str(file.relative_to(til_path))
        file_url = f"https://github.com/Azanul/til/blob/main/{file_path}"
        print(file_url)

        with file.open() as f:
            title = f.readline().lstrip("#").strip()
            date = file_times[str(file.relative_to(til_path))]["created_utc"].split("T")[0]

        tils.append(f"[{title}]({file_url}) - {date}")

    tils.append("<!-- tils ends -->")
    print(tils)

    readme = profile_path / "README.md"
    readme_contents = readme.open().read()

    tils_txt = "\n".join(tils).strip()
    rewritten = tils_pattern.sub(tils_txt, readme_contents)
    if "--rewrite" in sys.argv:
        readme.open("w").write(rewritten)
    else:
        print(tils_txt)


if __name__ == "__main__":
    update_tils(profile_path)
    # update_blogs(profile_path)
