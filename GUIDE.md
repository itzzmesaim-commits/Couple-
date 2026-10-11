# Playmates: update karne ke steps (har step mein 1 kaam)

## A. Firebase mein 2 cheezein (ek baar)
1. Email login ON: https://console.firebase.google.com/project/couples-ab32f/authentication/providers
   > **Email/Password** > Enable > Save.
2. Rules: https://console.firebase.google.com/project/couples-ab32f/firestore/databases/-default-/rules
   Purana text hatao, `firestore.rules` file ka poora text paste karo, **Publish**.
   (Is file mein `ADMIN_EMAIL_HERE` ki jagah tumhari email hogi.)

## B. GitHub par update
1. Repo mein purani `Couples-project.zip` ko naye zip se replace karo (Add file > Upload files, same naam).
2. `.github/workflows/build.yml` kholo > Edit > `build.yml` ka naya text paste karo > Commit. (Sirf ek baar.)
3. `join.html` ko repo ke root mein upload karo (invite link ke liye).
4. Actions > Build APK > Run workflow. 10 minute baad **Playmates-APK** download karo.

## C. Pehli baar app mein
Sign up (email + password) > email par verification link kholo > app mein "Maine verify kar liya" > naam aur avatar.
Owner Panel (🛡️) sirf tumhari admin email se dikhega.

## D. Room kaise chalta hai
Room banao > Invite dabake WhatsApp par code bhejo > partner Join karke code daale > dono ek hi room mein sab games chun sakte ho.
Bot ke saath khelne ke liye room ki zaroorat nahi (offline bhi chalta hai).

## Apna content
- Dares: `www/data/dares.json`, Quiz: `www/data/quiz.json`, Cards: `www/data/intimacy.json`
- Images: `www/assets/intimacy/male/` aur `female/` mein daalo, naam `intimacy.json` mein likho.
