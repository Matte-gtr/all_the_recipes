$(document).ready(function(){

    let newIngredientField = '<div><input name="ingredients" type="text" class="" /><button type="button" class="btn btn-outline-primary btn-sm remove-ingredient">-</button></div>';
    let newMethodField = '<div><input name="method" type="text" class="" /><button type="button" class="btn btn-outline-primary btn-sm remove-method">-</button></div>';
    let newToolField = '<div><input name="tools" type="text" class="" /><button type="button" class="btn btn-outline-primary btn-sm remove-tool">-</button></div>';

    $('.add-ingredient').click(function(){
            $('#ingredient-wrapper').append(newIngredientField);
    });

    $('#ingredient-wrapper').on('click', '.remove-ingredient', function(){
        $(this).parent('div').remove();
    });

    $('.add-method').click(function(){
            $('#method-wrapper').append(newMethodField);
    });

    $('#method-wrapper').on('click', '.remove-method', function(){
        $(this).parent('div').remove();
    });

    $('.add-tool').click(function(){
            $('#tools-wrapper').append(newToolField);
    });

    $('#tools-wrapper').on('click', '.remove-tool', function(){
        $(this).parent('div').remove();
    });

});