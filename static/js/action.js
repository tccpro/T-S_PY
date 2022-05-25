url = window.location.href
$('#max_price').keyup(function () {

    min_price = $('#min_price').val()
    max_price = $('#max_price').val()
    if (parseFloat(min_price)>=parseFloat(max_price)){
        $('.danger-text').removeClass('close-text')
        $('.apply-btn').attr("disabled",true)
    }else{
        $('.danger-text').addClass('close-text')
        $('.apply-btn').attr("disabled",false)

    }
})
$('.sort_condition').change(function () {
    new_url = set_params(url,'sorting',$(this).val())
    window.location.replace(new_url)
})
$('.per-page').change(function () {
    new_url = set_params(url,'per-page',$(this).val())
    window.location.replace(new_url)
})
$('.paging').click(function () {
    new_url = set_params(url,'page',$(this).data('value'))
    window.location.replace(new_url)
})

$('.category-item').click(function () {
    new_url = set_params(url,'category',$(this).data('category'))
    window.location.replace(new_url)
})
$('.apply-btn').click(function () {
    min_price = $('#min_price').val()
    max_price = $('#max_price').val()
    new_url = set_params(url,'min-price',min_price)
    new_url=set_params(new_url,'max-price',max_price)
    window.location.replace(new_url)

})

function set_params(url,param,value) {
    current_url = ''
    path = url.split('?')[0]
    if (url.includes('?')){
        c = '&'
        current_url = url.split('?')[1]
        params = current_url.split('&')
        is_founded = false
        for (i=0;i<params.length;i++){
            if (params[i].split('=')[0]==param){
                params[i] = `${param}=${value}`
                is_founded = true
            }
        }
        current_url = params.join(('&'))
        if(!is_founded){
            current_url+=`&${param}=${value}`
        }

    }else{
        current_url += `${param}=${value}`
    }
    return path +'?'+ current_url
}

$('.add-cart').click(function(){
    product_id = $(this).data('id')
    $(this).removeClass('btn-primary')
    $(this).addClass('btn-success')
    $(this).text('Added card')
    data={'product_id':product_id}
    add_url = '/order/add-cart/'
    response = post_data(add_url,data,update_badge)


})

function update_badge(response) {
    $('.badge-count').text(response.order_size)
    if (response.event=='added'){

    }else{
        $(`#pid${response.pid}`).addClass('btn-primary')
        $(`#pid${response.pid}`).removeClass('btn-success')
        $(`#pid${response.pid}`).text('Add to cart')
    }
}
function DeleteOrder(id) {
    $.ajax(
        {
            type:'GET',
            url:`/order/delete/${id}/`,
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            success : function (response) {
                console.log(response)
                $(`#tr${response.item_id}`).remove()
                $('.badge-count').text(response.item_count)
                $('.total').text(`${response.total_price}.00`)
                Toastify({
                    text: response.text,
                    className: "success",
                    style: {
                        background: "linear-gradient(to right, #00b09b, #96c93d)",
                    }
                }).showToast();
            }
        }

    )
}
function post_data(url,data,call_back) {
    $.ajax(
        {
            type:'POST',
            url:url,
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            data : JSON.stringify(data),
            success : call_back
        }

    )
}

$('.change-quantity').click(function () {
    data_id = $(this).data('product')
    data_action = $(this).data('action')
    let url_change_quantity = `/order/edit/`
    let data = {
        'item':data_id,
        'data_action':data_action,
    }
    post_data(url_change_quantity,data,item_quantity_change)
})

function item_quantity_change(response) {
    if(response.error==false){
        $(`#input${response.item_id}`).val(response.item_quantity)
        $(`#total${response.item_id}`).text(`$${response.total_price}`)
        $('.total').text(`$${response.total}`)
    }
}

$('.input-quantity').keyup(function () {
    value = $(this).val()
    data_id = $(this).data('product')
    data_action = 'onkeyup'
    let url_change_quantity = `/order/edit/`
    let data = {
        'item':data_id,
        'data_action':data_action,
        'value':value
    }
    post_data(url_change_quantity,data,item_quantity_change)
})
function order_edit(url,data) {
            $.ajax(
                {
                    type:'POST',
                    url:url,
                    headers:{
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrftoken,
                    },
                    data : JSON.stringify(data),
                    success : function (data) {
                        console.log(data)
                    }
                }

            )
        }