  var first = true;
  text_searched = false;
  function search(e){
    if (first){
      var text_search = $('#tx-search-main').val();
    }else{
      var text_search = $('#tx-search-header').val();
    }
    
    if ( text_search == ''){
    
        return false;
    }
    
    $.post('/load', {search : text_search}, function( data){
      
      if (data.num==0){
        $('#galeria').html('');
        $('#not_found').show();
      }else{
        $('#not_found').hide();
        if (first){
          first = false;
          $('#div-search').hide('slow');
          $('#main-tagcloud').hide();
          $('#tx-search-header').val( text_search );
          $('#div-search-header').show();
          $('#tx-search-header').focus();
        }
        
        $('#galeria').html(data.html);
      }
      text_searched = true;
    },'json');
  }

 
  $(document).ready( function(){
            
            $('.tag').live('click', function(e){
                e.preventDefault();
                var input = first ? $('#tx-search-main') : $('#tx-search-header');
                
                if (text_searched){
                     input.val(''); 
                     text_searched = false;  
                }
                
                var text = (input.val() == '') ? $(this).html() : input.val()+' '+$(this).html();
                input.val( text);
                input.focus();
            });
            
            $('#bt-search-main').click( search );
            
            $('#tx-search-main').keypress(function(e){
                if (e.keyCode==13){
                  search();
                }
            });
            
            $('#tx-search-header').keypress(function(e){
              if (e.keyCode == 13){
                search();
              }
              
            
            });
            $('#tx-search-main').val('');
            $('#tx-search-main').focus();
  });