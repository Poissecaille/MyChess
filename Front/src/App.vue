<template>
    <v-app>
        <v-app-bar
                app
                color="#000000"
                dark
                shrink-on-scroll
                prominent
                src="./assets/fondMyChess.jpg"
                fade-img-on-scroll>

<v-app-bar-nav-icon></v-app-bar-nav-icon> <!-- Add the menu symbol on the left -->

            <v-toolbar-title style="width: 30%">
                <v-row no-gutters>
                    <v-col cols="1" align-self="center">
                        <v-img
                                src="./assets/ChessTeam.jpg"
                                aspect-ratio="1"
                                max-width="30"
                        ></v-img>
                    </v-col>
                    <v-col cols="11">
                        <span class="font-family:Corsiva,font-weight-thin">MyChessMarket</span>
                    </v-col>
                </v-row>

            </v-toolbar-title>
                        <div class="flex-grow-1"></div>

            <v-slide-x-transition>
                <v-text-field
                        v-if="searchAvailable"
                        class="mr-2"
                        label="Search ..."
                        v-model="search"
                        clearable
                        single-line
                        light
                        solo
                >
                </v-text-field>
            </v-slide-x-transition>
            <v-btn icon>
                <v-icon @click="searchAvailable = !searchAvailable">mdi-magnify</v-icon>
            </v-btn>

            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>

            <v-btn icon> <!-- add the three dot botton -->
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
            <template v-slot:extension> <!-- make the top image larger and add menues -->
                <v-tabs
                        align-with-title
                        background-color="transparent">
                    <v-tab>Products</v-tab>
                    <v-tab>Category</v-tab>
                    <v-tab>Users</v-tab>
                </v-tabs>
            </template>

                <v-spacer></v-spacer>
                <v-btn text rounded>Home</v-btn>
                <v-row justify="center">
                <v-btn
                    text
                    rounded
                  @click.stop="logindialog = true"
                >
                  Login
                </v-btn>
                    <v-dialog
                  v-model="logindialog"
                  max-width="290"
                >
                        <v-card>
                    <v-card-title class="headline">Use Google's location service?</v-card-title>

                                        <!--login Module-->
                    <v-card width="400" class="ms-auto mt-5">
                    <v-card-title>
                        <h1 class="display-1">Login</h1>
                    </v-card-title>
                        <v-card-text>
                            <v-form>
                                <v-text-field
                                label="Username"
                                prepend-icon="mdi-account-circle"/>
                                <v-text-field
                                    :type="showPassword ? 'text': 'password'"
                                    label="Password"
                                    prepend-icon="mdi-lock"
                                    :append-icon="showPassword ? 'mdi-eye': 'mdi-eye-off'"
                                    @click:append="showPassword = !showPassword"
                                />
                            </v-form>
                        </v-card-text>
                        <v-card-action>
                            <v-btn color="success">Register</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="info">Login</v-btn>
                        </v-card-action>
                    </v-card>
                           <v-card-actions>
                      <div class="flex-grow-1"></div>
                            </v-card-actions>

                            </v-card>

                                        </v-dialog>


</v-row>


        </v-app-bar>

    <v-content>

<v-container>
                <product-list :search="search"></product-list>
            </v-container>

            <Product name="Echiquier acajou et sycomore 44 cm avec notations"/>
            <Product :name="product.name" v-for="product in products" :key="product.name"/>
        <router-view></router-view>
        </v-content>

    <!-- footbar -->
        <v-footer
    color="000000"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="black py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Copyright © 2019 MyChess Ltd - Paris
</strong>
      </v-col>
    </v-row>
    </v-footer>
    </v-app>
</template>

<!--<script>-->

<!--  import axios from 'axios';-->
<!--    import Product from './components/Product';-->

<!--    export default {-->
<!--        name: 'App',-->
<!--        components: {-->
<!--            Product,-->
<!--            // ProductList-->

<!--        },-->
<!--        data: () => ({//-->
<!--            search: null,-->
<!--            products: [],-->
<!--            showPassword: false, //for the login-->
<!--            links: [-->
<!--                'Home',-->
<!--                'Login'-->
<!--            ],-->

<!--            searchAvailable: false,-->
<!--            logindialog: false,-->


<!--        }),-->
<!--        created() {-->

<!--        },-->

<!--        methods:{-->
<!--            searchProducts()  {-->
<!--                let params = {query: this.search};-->
<!--                axios.get('http://localhost:8000/api/v1/products', {params: params}).then((response) => {-->
<!--                    this.products = response.data;-->
<!--                });-->
<!--            }-->
<!--        }-->


<!--    };-->
<!--</script>-->
