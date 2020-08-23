$(document).ready(function(){

    // Adds an ingredient field with remove button when "add ingredient" button is clicked (create/edit_recipe)
    $('.add-ingredient').click(function(){
        let newIngredientField = '<div><input name="ingredients" type="text" class="form-control short-field" />' +
        '<button type="button" class="btn btn-warning btn-sm remove-ingredient remove-button">-</button></div>';
        $('#ingredient-wrapper').append(newIngredientField);
    });

    // Removes the associated ingredient input field along with it's remove button (create/edit_recipe)
    $('#ingredient-wrapper').on('click', '.remove-ingredient', function(){
        $(this).parent('div').remove();
    });

    // Adds a method field with remove button when "add method step" button is clicked (create/edit_recipe)
    $('.add-method').click(function(){
        let newMethodField = '<div><input name="method" type="text" class="form-control mid-field" />' +
        '<button type="button" class="btn btn-warning btn-sm remove-method remove-button">-</button></div>';
        $('#method-wrapper').append(newMethodField);
    });

    // Removes the associated method input field along with it's remove button (create/edit_recipe)
    $('#method-wrapper').on('click', '.remove-method', function(){
        $(this).parent('div').remove();
    });

    // Adds a tool field with remove button when "add tool" button is clicked (create/edit_recipe)
    $('.add-tool').click(function(){
        let newToolField = '<div><input name="tools" type="text" class="form-control short-field" />' + 
        '<button type="button" class="btn btn-warning btn-sm remove-tool remove-button">-</button></div>';
        $('#tools-wrapper').append(newToolField);
    });

    // Removes the associated tool input field along with it's remove button (create/edit_recipe)
    $('#tools-wrapper').on('click', '.remove-tool', function(){
        $(this).parent('div').remove();
    });

});