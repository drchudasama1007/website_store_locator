from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class WebsiteController(http.Controller):

    @http.route(['/store-locator'], type='http', auth='public', website=True)
    def retail_page(self, **kwargs):
        api_key = request.website.google_maps_api_key
        locations = None
        store_country_id = None
        store_country = None
        countries = request.env['store.country'].sudo().search([])
        if countries:
            locations = request.env['store.location'].sudo().search([('store_country_id','=',countries[0].id)])
            store_country_id = countries[0].id
            store_country = countries[0]
        return request.render("website_store_locater.google_map_template", {
            'api_key': api_key,
            'locations': locations,
            'countries': countries,
            'store_country_id':store_country_id,
            'store_country':store_country,
        })

    @http.route(['/retail/<model("store.country"):store_country>'], type='http', auth='public', website=True)
    def retail_sub_page(self, store_country ,**kwargs):
        api_key = request.website.google_maps_api_key
        locations = request.env['store.location'].sudo().search([('store_country_id','=',store_country.id)])
        countries = request.env['store.country'].sudo().search([])
        return request.render("website_store_locater.google_map_template", {
            'api_key': api_key,
            'locations': locations,
            'countries': countries,
            'store_country_id': store_country.id,
            'store_country': store_country,
        })

    @http.route(['/store/location'], type='json', auth="public")
    def storeLocation(self, **kwargs):
        store_country_id = kwargs.get('store_country_id')
        locations = request.env['store.location'].search([('store_country_id','=',store_country_id)])
        lat_long_list = []
        for location in locations:
            list = []
            if location:
                list.append(location.lat)
                list.append(location.long)
                list.append(location.name)
                list.append(location.city)
                list.append(location.phone)
                list.append(location.id)
            lat_long_list.append(list)
        return lat_long_list

    @http.route(['/store/locator/marker'], type='json', auth="public")
    def searchmarker(self, **kwargs):
        markersid = kwargs.get('id')
        i = kwargs.get('i')
        markerid = request.env['store.location'].search([('id', '=', markersid)])
        markerid.markers_id = i
        return markerid;

    @http.route(['/map/key'], type='json', auth="public")
    def map_key(self, **kwargs):
        map_key = request.env['website'].get_current_website().google_maps_api_key
        return map_key

    @http.route('/advance_search_place', auth='public', website=True, type='json', csrf=False)
    def advance_search_place(self, **post):
        products = request.env['store.location'].sudo().search_read(
            [('name', 'ilike', post.get('product_search')),('store_country_id', '=', post.get('store_country_id'))])
        print("store_country_id========products========",products,post)
        return request.env['ir.ui.view'].render_template('website_store_locater.productsSearchBarSolution',
                                                         {'products': products})