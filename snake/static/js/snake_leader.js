$(document).ready(function(){

    $.ajax({
        url:'/leaderboard/',
        type: 'GET',
        dataType: 'html',
        success: function(response){
            console.log(response)
        },
        error: function(response){
            console.log(response)
        }
    })

});