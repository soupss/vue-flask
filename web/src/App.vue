<template>
    <nav class="navbar navbar-icon-top navbar-expand-lg navbar-dark bg-dark justify-content-center">
        <ul class="navbar-nav">
            <li class="nav-item">
                <router-link class="text-center nav-link" to="/articles">
                    <i class="fas fa-home"></i>
                    <br>
                    All Articles
                </router-link>
            </li>
            <li class="nav-item">
                <router-link class="text-center nav-link" to="/articles/new">
                    <i class="fas fa-plus"></i>
                    <br>
                    New Article
                </router-link>
            </li>
        </ul>
    </nav>
    <div class="container">
        <router-view :key="$route.path"/>
    </div>
</template>
