<template>
    <v-container>
        <v-layout v-if="product !== null">
            <v-flex xs12>
                <v-card class="mx-auto">
                    <v-list-item three-line>
                        <v-list-item-content>
                            <div class="overline mb-4">OVERLINE</div>
                            <v-list-item-title class="headline mb-1">{{ product.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ product.category }}</v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-avatar
                                tile
                                size="80"
                        >
<!--                            <v-img-->
<!--                                    :src="product.sprites_front"-->
<!--                                    aspect-ratio="1"-->
<!--                            ></v-img>-->
<!--                            <v-img-->
<!--                                    :src="product.sprites_back"-->
<!--                                    aspect-ratio="1"-->
<!--                            ></v-img>-->
                        </v-list-item-avatar>
                    </v-list-item>

                    <v-card-actions>
                        <v-chip v-for="category in product.categories" class="mx-1">{{ category }}
                        </v-chip>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';
/*export default est une classe */
    export default {
        props: ['name'],
        data: () => ({
            product: null
        }),
        created() {
            axios.get('http://localhost:8000/api/v1/product/' + this.name).then((response) => {
                this.product = response.data;
            });/*quand le serveur répond, la fonction s'execute=>then  this=self*/
        }
    };
</script>
