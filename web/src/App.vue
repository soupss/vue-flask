<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark justify-content-center">
        <ul class="navbar-nav nav">
            <li class="nav-item">
                <a class="text-center nav-link" to="/articles">
                    <i class="fas fa-map-marker-alt"></i>
                    <br>
                    {{ routeName }}
                </a>
            </li>
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

<script>
export default {
    computed: {
        routeName() {
            return this.$route.name
        }
    }
}
</script>
