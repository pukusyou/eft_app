
//pagetopのボタンを出したり消したりするスクリプト
$(function(){
    var scroll = $('.scroll');
    var scrollShow = $('.scroll-show');
        $(scroll).hide();
        $(window).scroll(function(){
            if($(this).scrollTop() >= 300) {
                $(scroll).fadeIn(500).addClass(scrollShow);
            } else {
                $(scroll).fadeOut(500).removeClass(scrollShow);
            }
        });
});

//スムーススクロールのスクリプト
$(function(){
  push()
    $('a[href^="#"]').click(function(){
        var href = $(this).attr('href');
        var target = href == '#' ? 0 : $(href).offset().top;
            $('body,html').animate({scrollTop:target},500);
            return false;
    });
});


(function() {
    const expire = 365; // 有効期限（日）
    let cc = document.querySelector('.cookie-consent');
    let ca = document.querySelector('.cookie-agree');
    const flag = localStorage.getItem('popupFlag');
    if (flag != null) {
      const data = JSON.parse(flag);
      if (data['value'] == 'true') {
        popup();
      } else {
        const current = new Date();
        if (current.getTime() > data['expire']) {
          setWithExpiry('popupFlag', 'true', expire);
          popup();
        }      
      }
    } else {
      setWithExpiry('popupFlag', 'true', expire);
      popup();
    }
    ca.addEventListener('click', () => {
      cc.classList.add('cc-hide1');
      setWithExpiry('popupFlag', 'false', expire);
    });
    
    function setWithExpiry(key, value, expire) {
      const current = new Date();
      expire = current.getTime() + expire * 24 * 3600 * 1000;
      const item = {
        value: value,
        expire: expire
      };
      localStorage.setItem(key, JSON.stringify(item));
    }
    
    function popup() {
      cc.classList.add('is-show');
    }
  }());

function push() {
  Push.create("Hideout機能追加にご協力ください！", {
    body: "アイテムの画像をアップロードしていただきたいです。",
    icon: '/icon.png',
    timeout: 4000,
    onClick: function () {
      window.open('https://twitter.com/SYTd_pukusyou/status/1620788232991707136', '_blank'); //URLリンク先
    }
});
}