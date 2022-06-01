/* 
    Created by Connor Harris (23208009) for CITS3403 final exam. 
*/

//Current page and tab shown. Defaults to the introduction overview page. 
var current_selected_class = "list_overview";
var current_showed_page = "overview_introduction_game_brief";

//Load the event listeners upon page load. 
window.onload = function(){
    document.getElementById("list_overview").addEventListener("click", overview_clicked);
    document.getElementById("list_overview_rules").addEventListener("click", overview_rules_clicked);
    document.getElementById("list_client_side").addEventListener("click", client_side_clicked);
    document.getElementById("list_server_side").addEventListener("click", server_side_clicked);
    document.getElementById("list_software_process").addEventListener("click", software_process_clicked);
}

//Selectors for each tab button pressed
function overview_clicked(){
    change_div("list_overview", "overview_introduction_game_brief"); }
function overview_rules_clicked(){
    change_div("list_overview_rules", "overview_introduction_game_rules"); }
function client_side_clicked(){
    change_div("list_client_side", "section_client-side"); }
function server_side_clicked(){
    change_div("list_server_side", "section_server-side"); }
function software_process_clicked(){
    change_div("list_software_process", "section_software-process"); }

//Change the display to the selected page, and reflect the change on the tab bar
function change_div(list_clicked, section_to_show) {
    //change tabs at the top for colour to displayed one
    document.getElementById(current_selected_class).classList.remove("current_list_item");
    document.getElementById(list_clicked).classList.add("current_list_item");
    current_selected_class = list_clicked;

    //change page being showed
    document.getElementById(current_showed_page).classList.add("no_display");
    document.getElementById(section_to_show).classList.remove("no_display");
    current_showed_page = section_to_show;
}