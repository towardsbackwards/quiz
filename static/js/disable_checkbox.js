// Функция для ограничения выбора только одного верного варианта ответа, если таков вопрос
$(document).on( 'change', '.field-correct :checkbox', function(){
    var $check = $(this),
        $div = $check.parent();
    if ($check.prop('checked') && $('#id_type').val() === '1') {
         $('[name~="choice"], [name$="correct"]').each(function() {
              if (!$(this).is(':checked')) {
              $(this).prop('disabled', true);
              }
              });
    } else {
         $('[name~="choice"], [name$="correct"]').each(function() {
              if (!$(this).is(':checked')) {
              $(this).prop('disabled', false);
              $(this).css('background-color', 'red');
              }
              });
    }
} );

$(document).on('change', '#id_type', function(){
    var $check = $('.field-correct :checked').prop('checked');
    if ($check && $('#id_type').val() === '1') {
         $('[name~="choice"], [name$="correct"]').each(function() {
              if (!$(this).is(':checked')) {
              $(this).prop('disabled', true);
              }
              });
    }
} );

$(document).ready(function(){
    var $check = $('.field-correct :checked').prop('checked');
        if ($check && $('#id_type').val() === '1') {
         $('[name~="choice"], [name$="correct"]').each(function() {
              if (!$(this).is(':checked')) {
              $(this).prop('disabled', true);
              }
              });
    }
} );