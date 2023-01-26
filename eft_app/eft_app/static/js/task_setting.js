jQuery(function(){
    var load_values = $.cookie("tasks").split(",");

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

