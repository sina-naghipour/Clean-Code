import os

def bundle_project(output_filename="project_bundle.txt", exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', '.venv', 'venv', '.idea', '.mypy_cache', '.pytest_cache'}
    if exclude_files is None:
        exclude_files = {output_filename, os.path.basename(__file__)}

    with open(output_filename, "w", encoding="utf-8") as bundle:
        for root, dirs, files in os.walk("."):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if file in exclude_files:
                    continue

                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    content = f"[Could not read file: {e}]"

                rel_path = os.path.relpath(path, ".")
                bundle.write(f"\n{'=' * 80}\n")
                bundle.write(f"File: {rel_path}\n")
                bundle.write(f"{'=' * 80}\n\n")
                bundle.write(content)
                bundle.write("\n\n")

    print(f"✅ Project bundled into '{output_filename}'")

if __name__ == "__main__":
    bundle_project()
