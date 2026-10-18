import datetime as dt
import os
import signal
import subprocess
import sys


PID_FILE = ".service.pid"
LOGS_DIR = "logs"
LOG_FILE = os.path.join(LOGS_DIR, "backup_manager.log")
SCHEDULES_FILE = "backup_schedules.txt"
BACKUPS_DIR = "backups"


def log(msg: str):
    os.makedirs(LOGS_DIR, exist_ok=True)
    now_str = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now_str}] {msg}\n")


def is_service_running() -> int | None:
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, "r") as f:
                pid = int(f.read().strip())
            os.kill(pid, 0)
            return pid
        except (OSError, ValueError):
            if os.path.exists(PID_FILE):
                os.remove(PID_FILE)
    return None


def cmd_start():
    pid = is_service_running()
    if pid is not None:
        log("Error: backup_service already running")
        return

    try:
        proc = subprocess.Popen(
            [sys.executable, "backup_service.py"],
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        with open(PID_FILE, "w") as f:
            f.write(str(proc.pid))
        log("backup_service started")
    except Exception:
        log("Error: can't start backup_service")


def cmd_stop():
    pid = is_service_running()
    if pid is None:
        log("Error: backup_service not running")
        return

    try:
        os.kill(pid, signal.SIGTERM)
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
        log("backup_service stopped")
    except Exception:
        log("Error: can't stop backup_service")


def cmd_create(schedule_str: str):
    parts = schedule_str.split(";")
    if len(parts) != 3 or not parts[0] or not parts[1] or not parts[2]:
        log(f"Error: malformed schedule: {schedule_str}")
        return

    time_parts = parts[1].split(":")
    if len(time_parts) != 2:
        log(f"Error: malformed schedule: {schedule_str}")
        return

    try:
        h, m = int(time_parts[0]), int(time_parts[1])
        if not (0 <= h < 24 and 0 <= m < 60):
            log(f"Error: malformed schedule: {schedule_str}")
            return
    except ValueError:
        log(f"Error: malformed schedule: {schedule_str}")
        return

    with open(SCHEDULES_FILE, "a", encoding="utf-8") as f:
        f.write(f"{schedule_str}\n")
    log(f"New schedule added: {schedule_str}")


def cmd_list():
    if not os.path.exists(SCHEDULES_FILE):
        log("Error: can't find backup_schedules.txt")
        return

    with open(SCHEDULES_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    for idx, line in enumerate(lines):
        print(f"{idx}: {line}")
    log("Show schedules list")


def cmd_delete(index_str: str):
    if not os.path.exists(SCHEDULES_FILE):
        log("Error: can't find backup_schedules.txt")
        return

    try:
        target_idx = int(index_str)
    except ValueError:
        log(f"Error: can't find schedule at index {index_str}")
        return

    with open(SCHEDULES_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if 0 <= target_idx < len(lines):
        deleted = lines.pop(target_idx)
        with open(SCHEDULES_FILE, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(f"{line}\n")
        log(f"Schedule at index {target_idx} deleted")
    else:
        log(f"Error: can't find schedule at index {target_idx}")


def cmd_backups():
    if not os.path.isdir(BACKUPS_DIR):
        log("Error: can't find backups directory")
        return

    files = sorted(os.listdir(BACKUPS_DIR))
    for fname in files:
        print(fname)
    log("Show backups list")


def main():
    if len(sys.argv) < 2:
        return

    command = sys.argv[1]
    if command == "start":
        cmd_start()
    elif command == "stop":
        cmd_stop()
    elif command == "create" and len(sys.argv) >= 3:
        cmd_create(sys.argv[2])
    elif command == "list":
        cmd_list()
    elif command == "delete" and len(sys.argv) >= 3:
        cmd_delete(sys.argv[2])
    elif command == "backups":
        cmd_backups()


if __name__ == "__main__":
    main()
