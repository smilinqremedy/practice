import datetime as dt
import os
import tarfile
import time


LOGS_DIR = "logs"
LOG_FILE = os.path.join(LOGS_DIR, "backup_service.log")
SCHEDULES_FILE = "backup_schedules.txt"
BACKUPS_DIR = "backups"


def log(msg: str):
    os.makedirs(LOGS_DIR, exist_ok=True)
    now_str = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now_str}] {msg}\n")


def perform_backup(path_to_save: str, backup_name: str):
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    tar_filename = f"{backup_name}.tar" if not backup_name.endswith(".tar") else backup_name
    tar_path = os.path.join(BACKUPS_DIR, tar_filename)

    try:
        with tarfile.open(tar_path, "w") as tar:
            if os.path.exists(path_to_save):
                tar.add(path_to_save, arcname=os.path.basename(path_to_save))
            else:
                # If path doesn't exist yet, create empty archive or add placeholder
                pass
        log(f"Backup done for {path_to_save} in backups/{tar_filename}")
    except Exception as e:
        log(f"Error: failed backup for {path_to_save}: {e}")


def run_cycle():
    if not os.path.exists(SCHEDULES_FILE):
        return

    now_hhmm = dt.datetime.now().strftime("%H:%M")
    with open(SCHEDULES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) == 3:
                path_to_save, sched_time, backup_name = parts[0], parts[1], parts[2]
                if sched_time == now_hhmm:
                    perform_backup(path_to_save, backup_name)


def main():
    while True:
        try:
            run_cycle()
        except Exception:
            pass
        time.sleep(30)


if __name__ == "__main__":
    main()
