# Fake update discord version
-------------------------------

In `/opt/discord-canary` (remove `-canary` for stable version or replace with `-ptb` for test release) edit the file `resources/build_info.json`
that should look like:

```json
{
  "releaseChannel": "canary", 
  "version": "0.0.xxx"
}
```

You can "upgrade" the version by replacing the `xxx` above with the latest version, and trick the launcher. All is reset in a future update.

ref: [Discord_asks_for_an_update_not_yet_available_in_the_repository](https://wiki.archlinux.org/title/Discord#Discord_asks_for_an_update_not_yet_available_in_the_repository)
