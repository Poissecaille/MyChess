<template>
    <div class="MyProduct">
        <v-card class="mx-auto" hover>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title class="display-1 text--primary mb-1">{{ product.name }}</v-list-item-title>
<!--                    <v-list-item-subtitle>{{ product.material }}</v-list-item-subtitle>-->
                    <v-list-item-subtitle>{{ product.category }}</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                        tile
                        size="80"
                >
<!--                    <v-img-->
<!--                            :src="product.sprite_front"-->
<!--                            aspect-ratio="1"-->
<!--                    ></v-img>-->
                </v-list-item-avatar>
            </v-list-item>

            <v-card-actions>
                <v-chip v-for="material in product.materials" class="mx-1" :key="material">{{ material }}</v-chip> //gère les icones en bas des éléments de la page
                <v-spacer></v-spacer>
                <v-btn text icon color="blue" @click="StartEditProduct"> //la couleur désigne le crayon, start edit product renvoit plus bas
                    <v-icon>edit</v-icon>
                </v-btn>
                <v-btn text icon color="red" @click="DeleteProduct"> //idem
                    <v-icon>delete</v-icon>
                </v-btn>
            </v-card-actions>
        </v-card>

        <v-row justify="center">
            <v-dialog v-model="edit" persistent max-width="600px">
                <v-card v-if="product_edited">
                    <v-card-title class="mb-1">
                        <span class="display-1">{{ product.name }}</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="6" md="4" v-for="category in Object.keys(product_edited.categories)" :key="category"> //modifie la largeur des cases des categories
                                    <v-text-field
                                            :label="category"
                                            v-model="product_edited.categories[category]"
                                            outlined
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-select
                                            v-model="product_edited.materials"
                                            :items="materials"
                                            chips
                                            label="Materials"
                                            multiple
                                            outlined
                                    ></v-select>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <div class="flex-grow-1"></div>
                        <v-btn color="grey darken-1" text @click="edit = false">Close</v-btn>
                        <v-btn color="primary" @click="EditProduct">Save</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-row>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['Product'],
        data: () => ({
            edit: false,
            Product_edited: null,
            materials: null
        }),
        methods: {
            StartEditProduct() {
                this.materials = [];
                this.Product_edited = {
                    categories: {},
                    materials: []
                };
                Object.keys(this.product.categories).forEach((category) => {
                    this.product_edited.categories[category] = this.product.categories[category];
                });
                this.product.materials.forEach((material) => {
                    this.product_edited.materials.push(material);
                    this.materials.push(material);
                });

                axios.get('http://localhost:8000/api/v1/materials').then((response) => {
                    this.materials = response.data;
                });

                this.edit = true;
            },
            EditProduct() {
                axios.patch('http://localhost:8000/api/v1/product/' + this.product.name, this.product_edited).then(() => {
                    this.$emit('update');
                });
            },
            Deleteproduct() {
                axios.delete('http://localhost:8000/api/v1/product/' + this.product.name).then(() => {
                    this.$emit('delete');
                });
            }
        }
    };
</script>
