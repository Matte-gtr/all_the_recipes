$(document).ready(function(){

    $('.add-ingredient').click(function(){
        let newIngredientField = '<div><input name="ingredients" type="text" class="form-control short-field" /><button type="button" class="btn btn-outline-primary btn-sm remove-ingredient remove-button">-</button></div>';
        $('#ingredient-wrapper').append(newIngredientField);
    });

    $('#ingredient-wrapper').on('click', '.remove-ingredient', function(){
        $(this).parent('div').remove();
    });

    $('.add-method').click(function(){
        let newMethodField = '<div><input name="method" type="text" class="form-control mid-field" /><button type="button" class="btn btn-outline-primary btn-sm remove-method remove-button">-</button></div>';
        $('#method-wrapper').append(newMethodField);
    });

    $('#method-wrapper').on('click', '.remove-method', function(){
        $(this).parent('div').remove();
    });

    $('.add-tool').click(function(){
        let newToolField = '<div><input name="tools" type="text" class="form-control short-field" /><button type="button" class="btn btn-outline-primary btn-sm remove-tool remove-button">-</button></div>';
        $('#tools-wrapper').append(newToolField);
    });

    $('#tools-wrapper').on('click', '.remove-tool', function(){
        $(this).parent('div').remove();
    });  

});