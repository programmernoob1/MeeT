$(document).ready(function(){
    $(document).on('click','.reqbtn',function () {
   var id;

   console.log('hello');
   id=$(this).attr('data-id');
   $.get('/home/sendreq',{id:id},function (data,status) {
       var item=$('#friend-change');
       item.html(data);
   })
});
   $(document).on('click','.accbtn',function ()  {
   var id;

   console.log('hello');
   id=$(this).attr('data-id');
   $.get('/home/accreq',{id:id},function (data,status) {
       var item=$('#friend-change');
       item.html(data);
   })
});
      $(document).on('click','.canbtn',function ()  {
   var id;

   console.log('hello');
   id=$(this).attr('data-id');
   $.get('/home/canreq',{id:id},function (data,status) {
       var item=$('#friend-change');
       item.html(data);
   })
});
});