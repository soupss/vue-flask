<template>
    <div class="container">
        <nav class="navbar navbar-expand-sm navbar-light bg-light">
            <div class="container-fluid">
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" id="categoriesDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Categories
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="categoriesDropdown">
                                <li> <router-link class="dropdown-item" to="/articles">All</router-link> </li>
                                <li> <router-link class="dropdown-item" to="/articles">Vehicles</router-link> </li>
                                <li> <router-link class="dropdown-item" to="/articles">Clothes</router-link> </li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/articles/new">New Article</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <router-view :key="$route.path"/>
    </div>
</template>
