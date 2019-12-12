function add_set_listener(){
    let all_set_buttons = document.querySelectorAll(".board_var_set_button");
    for(let i=0;i<all_set_buttons.length;i++){
        let set_button=all_set_buttons[i];
        let input_field = set_button.parentElement.querySelector("input");
        let var_name = input_field.getAttribute("name").replace("controller_variable_input_","");
        let position = parseInt(set_button.getAttribute("position"));
        let get_value = function(){
            switch (input_field.getAttribute("type")) {
                case "checkbox": return input_field.checked
                default:return input_field.value
            }
        }

        set_button.addEventListener("click", (e) => {
            ctrl('set_value',set_button.getAttribute("controller_id"),{'value':get_value(), 'name':var_name,'position':position});
        });
    }
}

add_set_listener();