import subprocess
import os
from shlex import split

from log import logger

CONFIG_FILE = "/config.txt"

if __name__ == "__main__":

    tasks = []

    with open(CONFIG_FILE) as f:
        for line in f:
            if not line.strip() or line.strip().startswith("#"):
                continue

            input_dir, output_dir = split(line)

            excludes_file = os.path.join(input_dir, ".stignore")
            if not os.path.exists(excludes_file):
                excludes_file = None

            tasks.append((input_dir, output_dir, excludes_file))

    for input_dir, output_dir, excludes_file in tasks:

        command = [
            "rsync",
            "-ra",
            "--delete",
            "--delete-excluded",
            "--stats",
        ]

        if excludes_file:
            command.append(f"--exclude-from={excludes_file}")

        command.append(input_dir)
        command.append(output_dir)

        logger.info(f"Copying {input_dir} to {output_dir}; {command}")
        result = subprocess.run(command)
        logger.info(f"rsync done (return code: {result.returncode})")
