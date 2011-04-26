/*
#       main.js     
#       
#       Copyright 2011 David <kippeld@gmail.com>            
#                      Arnau <sacaix@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
# 
*/

  var first = true;
  var text_searched = false;
  var search_from_hash = false;
  function search(e){
    if (e){
      e.preventDefault();
    }
    if (search_from_hash){
      var text_search = window.location.hash.substr(1).replace('+',' ');
      
      search_from_hash = false;
      window.location.hash = '';
            
    }else{
    
      var text_search = (first) ? $('#tx-search-main').val() : $('#tx-search-header').val();
    }
    if ( text_search == ''){
        alert('Heu de posar almenys una paraula de cerca');    
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
        $('.fotografia[rel]').overlay({
          mask: {
            color: '#ebecff',
            loadSpeed: 200,
            opacity: 0.4
          }
        });
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
                
                if (!first){
                  var wrapp = $('#tx-search-wrapper');
                  if ( ! wrapp.hasClass('resaltar')){
                  
                      wrapp.addClass('resaltar')
                      setTimeout( function(){
                        wrapp.removeClass('resaltar');
                      }, 1000);                    
                  }
                
                }
                
            });
            
            $('#bt-search-main').click( search );
            $('#bt-search-header').click(search);
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
            
            var hash = window.location.hash;
            
            if (hash.length > 1){
              
              search_from_hash = true;
              search();
            }
            
            
  });