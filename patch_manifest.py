import re, sys
p = 'android/app/src/main/AndroidManifest.xml'
x = open(p, encoding='utf-8').read()
if 'android:scheme="playmates"' not in x:
    f = '''
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="playmates" android:host="join" />
            </intent-filter>
'''
    x = x.replace('</activity>', f + '        </activity>', 1)
    open(p, 'w', encoding='utf-8').write(x)
print('manifest patched')
