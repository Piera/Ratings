$(document).ready(function()
    {
    
    $("#login").submit(userLogin);
    });

    
    function userLogin(username, password){
        $.post('hello',
            {'user_info': (username, password)},
                function (result)
                    console.log(result);

                }
            // {We will need to get some true/false value from the call back.}
            );
   

            alert("wth");

    }

    function confirm(e){
        e.preventDefault();
        alert("Im working");
    }

