jQuery(function () {
    if (getParam("check") != null) {
        var load_values = getParam("check");
    } else {
        var load_values = localStorage.getItem('tasks');
    }
    var load_values = decompressBinary(load_values)
    var count = 0;
    $("input[type=checkbox][name=task]").each(function () {
        if (load_values[count++] == 'A') {
            $(this).prop('checked', true);
        }

    });
});

$(document).on('click', 'input', function () {
    // console.log(save_values)
    localStorage.setItem('tasks', compress());
});

// var p_bool, t_bool, s_bool, pe_bool, m_bool, r_bool, j_bool = false
// 「全て選択」がクリックされたら

function all_check(dealer) {
    var bool
    var button_id = '#' + dealer + "_button"
    if ($(button_id).text() == "全選択") {
        bool = true
        $(button_id).text("選択解除")
        $(button_id).attr("class", "btn btn-info")
    } else {
        bool = false
        $(button_id).text("全選択")
        $(button_id).attr("class", "btn btn-primary")
    }
    var div_class = '.' + dealer + "_task"
    $(div_class).each(function () {
        if ($(this).css('display') != 'none') {
            $(this).find('.' + dealer).prop('checked', bool);
            localStorage.setItem('tasks', compress());
        }
    });
}
function compress() {
    var result = []
    $("input[type=checkbox][name=task]").each(function () {
        if (this.checked) {
            // チェック
            result.push('A')
        } else {
            result.push('B')
        }
    });
    return compressBinary(result.join(""))
}

//圧縮
function compressBinary(binary) {
    let result = "";
    let count = 1;
    for (let i = 1; i < binary.length; i++) {
        if (binary[i] === binary[i - 1]) {
            count++;
        } else {
            result += count + binary[i - 1];
            count = 1;
        }
    }
    result += count + binary[binary.length - 1];
    return result;
}

//展開
// ランレングス圧縮された2進数を展開する関数
function decompressBinary(compressedBinary) {
    let result = "";
    let count = "";
    if (compressedBinary != null) {
        for (let i = 0; i < compressedBinary.length; i++) {
            if (isNaN(parseInt(compressedBinary[i]))) {
                for (let j = 0; j < parseInt(count); j++) {
                    result += compressedBinary[i];
                }
                count = "";
            } else {
                count += compressedBinary[i];
            }
        }
        return result;
    }
}

$(document).on('click', '#setting', function () {
    $("#url").val("https://pukusyou.com/task/?check=" + compress());
    $(document).on('click', '#copy', function () {
        navigator.clipboard.writeText($("#url").val());
        $('.success-msg').fadeIn("slow", function () {
            $(this).delay(2000).fadeOut("slow");
        });
    });
});

function getParam(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function toggle(name) {
    all_dealer = ['prapor', 'therapist', 'skier', 'peacekeeper', 'mechanic', 'ragman', 'jaeger']
    all_dealer.forEach(dealer => {
        if (name == dealer || name == "all") {
            $("#" + dealer).show();
        } else {
            $("#" + dealer).hide();
        }
    });
}
$(document).on('input', '#prapor_search', function (e) {
    search("prapor")
});
$(document).on('input', '#therapist_search', function (e) {
    search("therapist")
});
$(document).on('input', '#skier_search', function (e) {
    search("skier")
});
$(document).on('input', '#peacekeeper_search', function (e) {
    search("peacekeeper")
});
$(document).on('input', '#mechanic_search', function (e) {
    search("mechanic")
});
$(document).on('input', '#ragman_search', function (e) {
    search("ragman")
});
$(document).on('input', '#jaeger_search', function (e) {
    search("jaeger")
});

function search(dealer) {
    $('.' + dealer + '_task').each(function () {
        if ($('#' + dealer + '_search').val().length <= 0) {
            $(this).show()
        } else if ($(this).find("label").text().toUpperCase().replace(" ", "").indexOf($('#' + dealer + '_search').val().toUpperCase().replace(" ", "")) == -1) {
            $(this).hide()
        } else {
            $(this).show()
        }
    });
}