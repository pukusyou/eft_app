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


$(function(){
  if ($("#fullname").text()=='MP-133') {
    driver.start();
  }
});

$(".toggle").on("click", function() {
  $(this).toggleClass("checked");
  $('.' + this.id).toggle();
  if(!$(this).find("input").prop("checked")) {
    $(this).find("input").prop("checked", true);
  } else {
    $(this).find("input").prop("checked", false);
  }
});