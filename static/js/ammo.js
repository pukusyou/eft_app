var default_value="All";
$(function(){$(".name").each(function(){var f=$(this).text();f=add_br(f,"mm;ACP;Lapua;MK 255;MK 318;.300;12/70".split(";"));$(this).html(f)});"Prapor_ll"in localStorage||(localStorage.setItem("Prapor_ll","Prapor.LL1"),localStorage.setItem("Skier_ll","Skier.LL1"),localStorage.setItem("Peacekeeper_ll","Peacekeeper.LL1"),localStorage.setItem("Mechanic_ll","Mechanic.LL1"),localStorage.setItem("Jaeger_ll","Jaeger.LL1"),localStorage.setItem("Workbench_lv","Workbench.lv1"));var b=localStorage.getItem("Prapor_ll"),
a=localStorage.getItem("Skier_ll"),c=localStorage.getItem("Peacekeeper_ll"),d=localStorage.getItem("Mechanic_ll"),e=localStorage.getItem("Jaeger_ll"),g=localStorage.getItem("Workbench_lv");b=[b,a,c,d,e,g];a="prapor skier peacekeeper mechanic jaeger workbench".split(" ");for(c=0;c<b.length;c++)$("#"+a[c]).text(b[c]);toggle_dealer();$("#ammoTable").tablesorter()});function add_br(b,a){a.forEach(c=>{b=b.replace(c,c+'<br class="d-sm-none"/>')});return b}
function dealer(b,a){$("#"+b).text(a);"prapor"==b?localStorage.setItem("Prapor_ll",a):"skier"==b?localStorage.setItem("Skier_ll",a):"peacekeeper"==b?localStorage.setItem("Peacekeeper_ll",a):"mechanic"==b?localStorage.setItem("Mechanic_ll",a):"jaeger"==b?localStorage.setItem("Jaeger_ll",a):"workbench"==b&&localStorage.setItem("Workbench_lv",a);toggle_dealer()}function ammo(b,a){$("#"+b).text(a);default_value=a;toggle_dealer()}
function toggle_dealer(){var b={All:"All","7.62x25mm":"7.62x25mm","9x18mm":"9x18mm","9x19mm":"9x19mm","9x21mm":"9x21mm",".357 Magnum":".357",".45 ACP":".45ACP","4.6x30mm":"4.6x30mm","5.7x28mm":"5.7x28mm","5.45x39mm":"5.45x39mm","5.56x45mm":"5.56x45mm","7.62x39mm":"7.62x39mm","9x39mm":"9x39mm","7.62x51mm":"7.62x51mm",".300 Blackout":".300","7.62x54mmR":"7.62x54mm",".338 Lapua Magnum":".338","12.7x55mm":"12.7x55mm","12.7x108mm":"12.7x108mm","12 gauge":"12/70","20 gauge":"20/70",".366 TKM":".366 TKM",
"23x75mm":"23x75mm"},a=/[^0-9]/g,c=localStorage.getItem("Prapor_ll").replace(a,""),d=localStorage.getItem("Skier_ll").replace(a,""),e=localStorage.getItem("Peacekeeper_ll").replace(a,""),g=localStorage.getItem("Mechanic_ll").replace(a,""),f=localStorage.getItem("Jaeger_ll").replace(a,"");a=localStorage.getItem("Workbench_lv").replace(a,"");var l=[[c,"Prapor.LL"],[d,"Skier.LL"],[e,"Peacekeeper.LL"],[g,"Mechanic.LL"],[f,"Jaeger.LL"],[a,"Workbench.LV"]];$(".ammo").each(function(){"All"==b[default_value]?
$(this).show():-1==$(this).find(".name").text().indexOf(b[default_value])?$(this).hide():$(this).show()});$(".ammo").each(function(){if("none"!=$(this).css("display")){var h=$(this).attr("class").split(" ");h.pop();var k=[];h.forEach(m=>{k.push(cheack(l,m))});k.includes(!0)?$(this).show():$(this).hide()}})}function cheack(b,a){const c=/[^0-9]/g;var d=!1;b.forEach(e=>{-1!=a.indexOf(e[1])&&Number(a.replace(c,""))<=Number(e[0])&&(d=!0)});return d};
