$(function () {
    $('.btn1').click(function () {
        $('.key').toggle();
    });
});

$(function(){
	// 変数に要素を入れる
	var open = $('.modal-open'),
		close = $('.modal-close'),
		container = $('.modal-container');

	//開くボタンをクリックしたらモーダルを表示する
	open.on('click',function(){	
		container.addClass('active');
		return false;
	});

    $("#loot").on("click", function() {
        $("#loot").toggleClass("checked");
        if(!$('input[name="check"]').prop("checked")) {
          $("#loot input").prop("checked", true);
        } else {
          $("#loot input").prop("checked", false);
        }
      });
      $("#key").on("click", function() {
        $("#key").toggleClass("checked");
        if(!$('input[name="check"]').prop("checked")) {
          $("#key input").prop("checked", true);
        } else {
          $("#key input").prop("checked", false);
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

    $('#loot').change(function() {
        console.log("Ok");
    });
});