var driver = new Driver({
  stageBackground: '#3d648a',
  nextBtnText: '次へ',
  prevBtnText: '戻る',
  closeBtnText: '閉じる',
  doneBtnText: '完了',
  padding: 5,
});

jQuery(function () {
  if (getParam("check") != null) {
    var load_values = getParam("check");
  } else {
    var load_values = $.cookie("tasks");
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
  $.cookie("tasks", compress());
});


// 「全て選択」がクリックされたら
$(document).on('click', '[id$="_button"]', function () {
  var className = "." + this.id.replace("_button", "");
  var bool = window[this.id.replace("_button", "_bool")];
  window[this.id.replace("_button", "_bool")] = all_check(className, bool);
});

function all_check(checkbox_class, bool) {
  $(checkbox_class).prop('checked', !bool);
  $.cookie("tasks", compress());
  return !bool;
}


driver.defineSteps([
  {
    element: '#prapor', // ハイライトさせる要素
    popover: {
      title: '1.タスクを選択',
      description: '各ディーラーの完了しているタスクにチェックします',
      position: 'right',
    }
  },
  {
    element: '#prapor_button',
    popover: {
      title: '2.全選択',
      description: '全選択、選択解除することができます',
    }
  },
  {
    element: '#submit',
    popover: {
      title: '3.決定',
      description: '完了したタスクを選択し終えたら決定します',
      position: 'left',
    }
  }
]);

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

$(document).on('click', '#setting', function () {
  $("#url").val("https://pukusyou.com/hideout/?check=" + compress());
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