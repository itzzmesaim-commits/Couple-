# Couples App: APK banane ka Guide (free)

Sab kuch free hai: GitHub (APK build), Firebase Spark plan (chat, leaderboard). Credit card nahi chahiye.

## Step 1: GitHub account aur repo
1. https://github.com par free account banao.
2. Upar `+` > **New repository**. Naam: `couples`. **Private** rakho (private bhi free hai, 2000 build minutes/mahina).
3. Repo ban jaaye to **uploading an existing file** link par click karo.
4. Is zip ke andar ka **saara content** (folders `www`, `assets`, `.github`, aur files `package.json`, `capacitor.config.json`, `firestore.rules`) drag-drop karo.
   - Dhyan: `.github` folder hidden hota hai. Agar upload mein nahi ja raha, to GitHub Desktop ya git use karo (neeche).
5. **Commit changes** dabao.

Git se (computer par): 
```
git init
git add .
git commit -m "Couples app"
git branch -M main
git remote add origin https://github.com/TUMHARA-NAAM/couples.git
git push -u origin main
```

## Step 2: Firebase (free) setup
1. https://console.firebase.google.com par Google account se login.
2. **Create project** > naam `couples` > Google Analytics **off** > Create.
3. Left menu **Build > Authentication > Get started > Sign-in method > Anonymous > Enable > Save**.
4. **Build > Firestore Database > Create database** > location `asia-south1 (Mumbai)` > **Production mode** > Create.
5. Firestore ke **Rules** tab mein jaao. Purana text hatao. Is repo ki `firestore.rules` file ka poora text paste karo > **Publish**.
6. **Project settings** (gear icon) > **Your apps** > **Web (`</>`)** > app nickname `couples` > Register app.
7. Jo `firebaseConfig = {...}` dikhe uski 6 values copy karo.
8. GitHub repo mein `www/js/firebase-config.js` kholo > pencil icon (edit) > `PASTE_HERE` ki jagah apni values daalo > **Commit changes**.

Photos Firestore mein chhoti (compressed) hoke save hoti hain, isliye Firebase Storage (paid) ki zaroorat nahi.

## Step 3: APK banao
1. Repo mein **Actions** tab kholo. Agar "Enable workflows" dikhe to dabao.
2. Left mein **Build APK** > **Run workflow** > Run. (Commit karne par ye apne aap bhi chalta hai.)
3. Lagbhag 6 to 10 minute lagte hain. Green tick aane par us run par click karo.
4. Neeche **Artifacts** mein **Couples-APK** download karo (zip). Unzip karo to `app-debug.apk` milega.

## Step 4: Phone par install
1. APK ko phone par bhejo (WhatsApp, Drive, cable).
2. Open karo. "Install unknown apps" ki permission do. Install.
3. App kholo, naam aur avatar chuno. Dono partners ke phone par install karo.
4. Ek player **Room banao** se code banaye, doosra **Join** mein code daale. Ya dono **Quick Match** dabayein.

## Apne questions, dares aur images daalna
- **Dares:** `www/data/dares.json`, ek list of text. Apne 50+ dares isme likho.
- **Quiz:** `www/data/quiz.json`, format: `{ "q": "sawal", "o": ["A","B","C","D"], "a": 2 }`. `a` (sahi option ka number, 0 se shuru) hata do to dono ka jawab same hone par point milta hai.
- **Intimacy cards (text):** `www/data/intimacy.json` ke `cards` mein.
- **Images (apni):** files `www/assets/intimacy/male/` aur `www/assets/intimacy/female/` mein daalo, phir `intimacy.json` mein naam likho: `"male": ["1.jpg","2.jpg"]`.
- Har change ke baad GitHub par commit karo. APK naya ban jaayega.

## Age verification
Adult Quiz, Punishment aur Intimacy Cards kholne se pehle date of birth maangi jaati hai (18+ zaroori) aur har baar confirm popup aata hai. Ye self-declared check hai, jitna imandari se bharo utna kaam karta hai.

## Zaroori baatein
- APK sirf apne aur partner ke use ke liye hai. **Google Play par adult content wali app allow nahi hoti.**
- Login anonymous hai: app uninstall karne par profile aur points chale jaate hain. Agle batch mein email login jod sakte hain.
- Abhi push notification nahi hai (chat tabhi dikhti hai jab app khula ho). Ye bhi agle batch mein.
- Firebase Spark plan ki free limit (roz 50,000 reads, 20,000 writes) do-chaar logon ke liye kaafi hai.
- Agar GitHub Actions use nahi karna: **Codemagic** ya **Expo EAS** free plan, ya computer par Android Studio (free) se `npx cap add android && npx cap sync && npx cap open android`.

## Is batch mein games
Tic Tac Toe, Checkers, 4 in a Row, Reversi, Dots & Boxes, Dice Party, Ludo, Adult Quiz, Punishment, Intimacy Cards.
Baaki games agle batches mein aayenge.

## Error aaye to
- App mein "Setup baaki hai": `firebase-config.js` mein keys nahi daali.
- "Login fail": Firebase mein Anonymous sign-in enable nahi kiya.
- Chat/leaderboard khaali: Firestore rules publish nahi kiye.
- Build fail: Actions mein red run kholo, log ka last error mujhe bhej do.
