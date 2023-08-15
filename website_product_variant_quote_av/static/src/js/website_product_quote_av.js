odoo.define('website_product_variant_quote_av.request_quote_btn', function(require) {
	"use strict";

	var publicWidget = require('web.public.widget');
	var rpc = require('web.rpc');
	var ajax = require('web.ajax');


	publicWidget.registry.websiteQuotation = publicWidget.Widget.extend({
		selector: '.oe_website_sale',
		events: {    
			'click .js_update_quote_prod': '_onClickQuotationQty',
			'click .request_quote_btn':'_onRequestQuoteBtn',
		},
		start: function(){
			const def = this._super(...arguments);
			$(".has_quote_product").find("a.a-submit").addClass("d-none");
			return def
		},
		/* Update quotation product qty */
		_onClickQuotationQty: function (ev) {
			var crr_qty = $(ev.currentTarget).parents(".css_quantity").find(".quotation_qty");
			var crr_val = crr_qty.val();
			var updated_val;
			if($(ev.currentTarget).hasClass("remove_one")){
				if (parseInt(crr_val) == 1){
					var updated_val = 1;
				}else{
					var updated_val = parseInt(crr_val) - 1;
				}
			}else{
				var updated_val = parseInt(crr_val) + 1;
			}
			var product_id = crr_qty.attr('data-product-id');
			
			ajax.jsonRpc("/quote/cart/update_json","call",{'product_id':product_id,'updated_val' : updated_val,
			}).then(function (data) {
				crr_qty.val(updated_val);
			});
		},

		/* Delete quotation product */
		_onRequestQuoteBtn: function () {
			var product_id = $(".product_id").val();
			$('.request_quote_form').attr('action','/quote/product/selected/'+product_id);
  			$('.request_quote_form').submit();
		}
	});
});
