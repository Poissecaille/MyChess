<template>
    <v-slide-y-transition
            mode="in-out"
            class="row py-2"
            group
            tag="div"
    >
        <v-col cols="6" v-for="product in products" :key="product.name">
            <Product :product="product" @delete="deleteProduct(product)"
                     @update="updateProduct(product)"/>
        </v-col>
    </v-slide-y-transition>
</template>

<script>
    import axios from 'axios';
    import Product from './Chess';

    export default {
        name: "ProductList",
        props: ['search'],
        data: () => ({
            products: []
        }),
        components: {
            Product,
        },
        watch: {
            search() {
                this.searchProducts();
            }
        },
        created() {
            this.searchProducts();
        },
        methods: {
            searchProducts() {
                let search = this.search;
                if (!search) {
                    search = "";
                }

                let params = {query: search};
                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {
                    this.products = response.data;
                });
            },
            updateProduct(product) {
                axios.get('http://localhost:8000/api/v1/products/' + product.name).then((response) => {
                    let index_of_products = this.products.indexOf(product);

                    let new_product = response.data;
                    this.products.splice(index_of_products, 1, new_product);
                });
            },
            deleteProduct(product) {
                let index_of_product = this.products.indexOf(product);
                this.products.splice(index_of_product, 1);
            }
        }
    }
</script>

<style scoped>

</style>