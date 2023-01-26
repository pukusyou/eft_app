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
    element: '.modal-open', // ハイライトさせる要素
    popover: {
      title: '1.表示設定',
      description: 'アイテムの表示・非表示のオプションを選択できます',
      position: 'right',
      }
   }
   ]);

function toggle_element(classname) {
        $(classname).toggle();
}

$(function(){
	// 変数に要素を入れる
	var open = $('.modal-open'),
		close = $('.modal-close'),
		container = $('.modal-container');

    if ($("#fullname").text()=='MP-133') {
      driver.start();
    }
	//開くボタンをクリックしたらモーダルを表示する
	open.on('click',function(){	
		container.addClass('active');
		return false;
	});

    $("#loot").on("click", function() {
        $("#loot").toggleClass("checked");
        toggle_element('.loot');
        if(!$('#loot_in').prop("checked")) {
          $("#loot input").prop("checked", true);
        } else {
          $("#loot input").prop("checked", false);
        }
      });
      $("#key").on("click", function() {
        $("#key").toggleClass("checked");
        toggle_element('.key');
        if(!$('#key_in').prop("checked")) {
          $("#key input").prop("checked", true);
        } else {
          $("#key input").prop("checked", false);
        }
      });
      $("#wepon").on("click", function() {
        $("#wepon").toggleClass("checked");
        toggle_element('.wepon');
        if(!$('#wepon_in').prop("checked")) {
          $("#wepon input").prop("checked", true);
        } else {
          $("#wepon input").prop("checked", false);
        }
      });

	//閉じるボタンをクリックしたらモーダルを閉じる
	close.on('click',function(){	
		container.removeClass('active');
	});

	//モーダルの外側をクリックしたらモーダルを閉じる
	$(document).on('click',function(e) {
		if(!$(e.target).closest('.modal-body').length) {
			container.removeClass('active');
		}
	});
});