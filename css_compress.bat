@echo off

for %%f in (ammo.css base.css hideout_item.css hideout_setting.css hideout_setting_en.css index.css privacy_policy.css task_item.css task_setting.css task_setting_en.css) do (
    echo %%f
    java -jar .\closure-compiler-v20230206.jar --css .\static\css\%%f --output-file ./static/css/comp/%%f
)