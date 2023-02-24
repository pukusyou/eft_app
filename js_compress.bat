@echo off

for %%f in (ammo.js contact.js contact_en.js hideout_item.js hideout_item_en.js hideout_setting.js hideout_setting_en.js index.js popper.min.js task_item.js task_item_en.js task_setting.js task_setting_en.js) do (
    echo %%f
    java -jar .\closure-compiler-v20230206.jar --js .\static\js\%%f --js_output_file ./static/js/comp/%%f
)