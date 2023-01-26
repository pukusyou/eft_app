var driver = new Driver({
    stageBackground: '#3d648a',
    nextBtnText: '次へ',
    prevBtnText: '戻る',
    closeBtnText: '閉じる',
    doneBtnText: '完了',
    padding: 5, 
});

jQuery(function(){
    var load_values = $.cookie("tasks").split(",");
    if (!load_values.includes("Debut")) {
        driver.start();
    }
    for(var i = 0; i < load_values.length; ++i){
        load_values[i] = decodeURIComponent(load_values[i]);
    }

    $("input[type=checkbox][name=task]").each(function(){
        this.checked = $.inArray(this.value, load_values) != -1;
    });
  });

$(document).on('click', 'input', function(){
    var save_values = [];

    $("input[type=checkbox][name=task]").each(function(){
        this.checked && save_values.push(encodeURIComponent(this.value));
    });

    $.cookie("tasks", save_values.join(","));
  });
  
  var p_bool, t_bool, s_bool, pe_bool, m_bool, r_bool, j_bool = false
  
  // 「全て選択」がクリックされたら
$(document).on('click', '#prapor_button', function(){
    p_bool = all_check('.prapor',p_bool);
  });

$(document).on('click', '#therapist_button', function(){
    t_bool = all_check('.therapist',t_bool);
});
$(document).on('click', '#skier_button', function(){
    s_bool = all_check('.skier',s_bool);
  });

$(document).on('click', '#peacekeeper_button', function(){
    pe_bool = all_check('.peacekeeper',pe_bool);
});
$(document).on('click', '#mechanic_button', function(){
    m_bool = all_check('.mechanic',m_bool);
  });

$(document).on('click', '#ragman_button', function(){
    t_bool = all_check('.ragman',t_bool);
});
$(document).on('click', '#jaeger_button', function(){
    t_bool = all_check('.jaeger',t_bool);
});

function all_check(checkbox_class, bool) {
    if (!bool) {
        // チェックされていたら全ての個別チェックボックスを選択状態に
        $(checkbox_class).prop('checked', true);
        var result = true
      } else {
        // チェックされていなければ全ての個別チェックボックスを選択解除
        $(checkbox_class).prop('checked', false);
        var result = false
      }
      var save_values = [];

      $("input[type=checkbox][name=task]").each(function(){
          this.checked && save_values.push(encodeURIComponent(this.value));
      });
  
      $.cookie("tasks", save_values.join(","));

      return result
}
$(document).on('click', '#tyuto', function(){
    
});

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

