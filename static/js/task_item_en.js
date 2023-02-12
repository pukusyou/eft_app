var driver = new Driver({
  stageBackground: '#3d648a',
  nextBtnText: '次へ',
  prevBtnText: '戻る',
  closeBtnText: '閉じる',
  doneBtnText: '完了',
  padding: 5,
});


driver.defineSteps([
  {
    element: '#setting', // ハイライトさせる要素
    popover: {
      title: '1.表示設定',
      description: 'アイテムの表示・非表示のオプションを選択できます',
      position: 'right',
    }
  }
]);

$(".toggle").on("click", function () {
  $(this).toggleClass("checked");
  $('.' + this.id).toggle();
});

$("#select").on("click", function () {
  var toleger = true;
  var bigBox_list = []
  var back_button = $("#back_zone").html();
  $("#setting").hide();
  $("#select").hide();
  $(".bigBox").css("border", "6px solid white")
  $("#back_zone").html('<button type="button" class="btn btn-success mb-12 border-primary" id="completion">Show only selected images</button>')
  $("#back_zone").append('<button type="button" class="btn btn-success mb-12 border-primary" id="all_completion">Show selection</button>')
  $(".bigBox").on("click", function () {
    if (!toleger) {
      return;
    }
    var result = object_iqual(bigBox_list, $(this))
    if (result[0]) {
      bigBox_list = result[1]
      $(this).css("border", "6px solid white")
    } else {
      bigBox_list.push($(this))
      $(this).css({ "border": "solid 6px #006400", "box-sizing": "border-box" });
    }
  });
  $("#completion").on("click", function () {
    if (bigBox_list != 0) {
      $(".bigBox").hide();
      $("#setting").hide();
      $("#select").hide();
      bigBox_list.forEach(element => {
        var clone = $(element.find("img")[0]).clone()
        $("#only_img_area").append(clone);
      });
      $("#back_zone").html('<button type="button" class="btn btn-success mb-12 border-primary" id="itiran_back">Return to list</button>')
      $("#itiran_back").on("click", function () {
        $("#only_img_area").empty();
        $(".bigBox").css({ "border": "", "box-sizing": "" })
        $(".bigBox").show();
        $("#setting").show();
        $("#select").show();
        $("#back_zone").html(back_button)
        $(".toggle").addClass("checked");
        toleger = false
      });
    } else {
      $(".bigBox").css("border", "")
      $("#back_zone").html(back_button)
      $("#setting").show();
      $("#select").show();
      toleger = false
    }

  });

  //boxごと
  $("#all_completion").on("click", function () {
    if (bigBox_list != 0) {
      $(".bigBox").hide();
      $("#setting").hide();
      $("#select").hide();
      var count = 0;
      bigBox_list.forEach(element => {
        var clone = $(element).clone()
        $("#only_img_area").append('<div class="bigBox ' + String(count) + '">');
        $(".bigBox" + "." + String(count)).append(clone.html());
        count++;
      });
      $("#back_zone").html('<button type="button" class="btn btn-success mb-12 border-primary" id="itiran_back">Return to list</button>')
      $("#itiran_back").on("click", function () {
        $("#only_img_area").empty();
        $(".bigBox").css({ "border": "", "box-sizing": "" })
        $(".bigBox").show();
        $("#setting").show();
        $("#select").show();
        $("#back_zone").html(back_button)
        console.log("ok")
        $(".toggle").addClass("checked");
        toleger = false
      });
    } else {
      $(".bigBox").css("border", "")
      $("#back_zone").html(back_button)
      $("#setting").show();
      $("#select").show();
      toleger = false
    }
  });
});

function object_iqual(array, num) {
  var result = [false, array]
  var index = 0
  array.forEach(element => {
    var elem_img = String(element.find("img").attr("src"))
    var num_img = String(num.find("img").attr("src"))
    if (elem_img == num_img) {
      result[1].splice(index, 1);
      result[0] = true;
    }
    index++;
  });
  return result;
}