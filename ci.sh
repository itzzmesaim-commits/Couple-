#!/bin/bash
# Runs inside GitHub Actions after the zip is extracted
set -e
cd "$(dirname "$0")"
npm install
npx cap add android
python3 scripts/patch_manifest.py
npx @capacitor/assets generate --android
npx cap sync android
cd android
chmod +x gradlew
./gradlew assembleDebug
