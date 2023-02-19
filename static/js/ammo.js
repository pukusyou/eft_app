var default_value = "All"
$(function () {
    $('.name').each(function () {
        var name = $(this).text()
        let trg = ['mm', 'ACP', 'Lapua', 'MK 255', 'MK 318', '.300', '12/70']
        name = add_br(name, trg)
        $(this).html(name)
    });
    if (!("Prapor_ll" in localStorage)) {
        localStorage.setItem("Prapor_ll", "Prapor.LL1");
        localStorage.setItem("Skier_ll", "Skier.LL1");
        localStorage.setItem("Peacekeeper_ll", "Peacekeeper.LL1");
        localStorage.setItem("Mechanic_ll", "Mechanic.LL1");
        localStorage.setItem("Jaeger_ll", "Jaeger.LL1");
        localStorage.setItem("Workbench_lv", "Workbench_lv1");
    }
    var prapor_ll = localStorage.getItem('Prapor_ll')
    var skier_ll = localStorage.getItem('Skier_ll')
    var peacekeeper_ll = localStorage.getItem('Peacekeeper_ll')
    var mechanic_ll = localStorage.getItem('Mechanic_ll')
    var jaeger_ll = localStorage.getItem('Jaeger_ll')
    var workbench_lv = localStorage.getItem('Workbench_lv')
    var storage_list = [prapor_ll, skier_ll, peacekeeper_ll, mechanic_ll, jaeger_ll, workbench_lv]
    var dealer_list = ['prapor', 'skier', 'peacekeeper', 'mechanic', 'jaeger', "workbench"]
    for (let index = 0; index < storage_list.length; index++) {
        $("#" + dealer_list[index]).text(storage_list[index])
    }
    toggle_dealer()
    $("#ammoTable").tablesorter();
});

function add_br(name, trg) {
    trg.forEach(element => {
        name = name.replace(element, element + '<br class="d-sm-none"/>')
    });
    return name
}

function dealer(character, level) {
    $("#" + character).text(level)
    if (character == "prapor") {
        localStorage.setItem("Prapor_ll", level)
    } else if (character == "skier") {
        localStorage.setItem("Skier_ll", level)
    } else if (character == "peacekeeper") {
        localStorage.setItem("Peacekeeper_ll", level)
    } else if (character == "mechanic") {
        localStorage.setItem("Mechanic_ll", level)
    } else if (character == "jaeger") {
        localStorage.setItem("Jaeger_ll", level)
    } else if (character == "workbench") {
        localStorage.setItem("Workbench_lv", level)
    }
    toggle_dealer()

}

function ammo(id, value) {
    $("#" + id).text(value)
    default_value = value
    toggle_dealer()
}
function toggle_dealer() {
    var ammo_value = { "All": "All", '7.62x25mm': '7.62x25mm', '9x18mm': '9x18mm', '9x19mm': '9x19mm', '9x21mm': '9x21mm', '.357 Magnum': '.357', '.45 ACP': '.45ACP', '4.6x30mm': '4.6x30mm', '5.7x28mm': '5.7x28mm', '5.45x39mm': '5.45x39mm', '5.56x45mm': '5.56x45mm', '7.62x39mm': '7.62x39mm', '9x39mm': '9x39mm', '7.62x51mm': '7.62x51mm', '.300 Blackout': '.300', '7.62x54mmR': '7.62x54mm', '.338 Lapua Magnum': '.338', '12.7x55mm': '12.7x55mm', '12.7x108mm': '12.7x108mm', '12 gauge': '12/70', '20 gauge': '20/70', '.366 TKM': '.366 TKM', '23x75mm': '23x75mm' }
    const regex = /[^0-9]/g;
    var prapor_ll = localStorage.getItem("Prapor_ll").replace(regex, "")
    var skier_ll = localStorage.getItem("Skier_ll").replace(regex, "")
    var peacekeeper_ll = localStorage.getItem("Peacekeeper_ll").replace(regex, "")
    var mechanic_ll = localStorage.getItem("Mechanic_ll").replace(regex, "")
    var jaeger_ll = localStorage.getItem("Jaeger_ll").replace(regex, "")
    var workbench_lv = localStorage.getItem("Workbench_lv").replace(regex, "")
    var dealer_ll = [[prapor_ll, "Prapor.LL"], [skier_ll, "Skier.LL"], [peacekeeper_ll, "Peacekeeper.LL"], [mechanic_ll, "Mechanic.LL"], [jaeger_ll, "Jaeger.LL"], [workbench_lv, "Workbench.LV"]]
    $(".ammo").each(function () {
        if (ammo_value[default_value] == "All") {
            $(this).show()
        } else {
            if ($(this).find(".name").text().indexOf(ammo_value[default_value]) == -1) {
                $(this).hide()
            } else {
                $(this).show()
            }
        }
    });
    $(".ammo").each(function () {
        if ($(this).css('display') != 'none') {
            var class_list = $(this).attr("class").split(" ")
            class_list.pop()
            var bool_list = []
            class_list.forEach(element => {
                bool_list.push(cheack(dealer_ll, element))
            });
            if (bool_list.includes(true)) {
                $(this).show()
            } else {
                $(this).hide()
            }
        }
    });

}
function cheack(dealer, class_tag) {
    const regex = /[^0-9]/g;
    var result = false
    dealer.forEach(element => {
        if (class_tag.indexOf(element[1]) != -1) {
            if (Number(class_tag.replace(regex, "")) <= Number(element[0])) {
                result = true
            }
        }
    });
    return result
}