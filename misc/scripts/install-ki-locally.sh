#!/bin/bash
# This script is intended to be executed with wget -O - <url> | bash

# Check if JDK 11 or higher is installed
if ! command -v java &> /dev/null; then
    echo "Error: JDK 11 or higher is not installed. Please install it and try again."
    exit 1
fi

# Check if the version of Java is 11 or higher
java_version=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}')
if [[ "${java_version%%.*}" -lt 11 ]]; then
    echo "Error: JDK 11 or higher is required. Detected version is $java_version."
    exit 1
fi

# Check if wget and unzip commands are available
if ! command -v wget &> /dev/null || ! command -v unzip &> /dev/null; then
    echo "Error: Both wget and unzip commands are required for this installation script."
    exit 1
fi

# Define URLs and file names
download_url="https://github.com/Kotlin/kotlin-interactive-shell/releases/download/v0.5.2/ki-archive.zip"
checksum_url="https://github.com/Kotlin/kotlin-interactive-shell/releases/download/v0.5.2/checksums_sha256.txt"
zip_file="/tmp/ki-archive.zip"
extracted_folder="/tmp/ki"

# Define target directory
target_dir="$HOME/.local"

# Download the zip file
wget "$download_url" -O "$zip_file"

# Download the checksum file
wget "$checksum_url" -O "/tmp/checksums_sha256.txt"

# Verify the checksum
expected_checksum=$(grep "ki-archive.zip" "/tmp/checksums_sha256.txt" | cut -d ' ' -f 1)
actual_checksum=$(sha256sum "$zip_file" | cut -d ' ' -f 1)

if [[ "$expected_checksum" != "$actual_checksum" ]]; then
    echo "Error: Checksum verification failed. Aborting installation."
    rm "$zip_file" # Remove the downloaded zip file
    exit 1
fi

# Extract the archive
unzip "$zip_file" -d "/tmp"

# Create target directories if they don't exist
mkdir -p "$target_dir/bin"
mkdir -p "$target_dir/lib"

# Move the files to the target directory
mv "$extracted_folder/bin/ki" "$target_dir/bin/"
mv "$extracted_folder/bin/ki.bat" "$target_dir/bin/"
mv "$extracted_folder/bin/ki.sh" "$target_dir/bin/"
mv "$extracted_folder/lib/ki-shell.jar" "$target_dir/lib/"

# Clean up - remove the extracted folder and zip file
rm -r "$extracted_folder"
rm "$zip_file"

# Clean up - remove checksum file
rm "/tmp/checksums_sha256.txt"

# Add warning if directory is not in PATH
if [[ ":$PATH:" != *":$target_dir/bin:"* ]]; then
    echo "Warning: The directory $target_dir/bin is not in your PATH."
    echo "You can add it by adding the following line to your ~/.bashrc or ~/.bash_profile file:"
    echo "export PATH=\$PATH:$target_dir/bin"
    echo "Then, either reopen your terminal or run 'source ~/.bashrc' (or 'source ~/.bash_profile')."
fi

echo "Installation completed successfully!"
