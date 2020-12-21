<template>
    <nav class="navbar navbar-dark bg-dark justify-content-center">
        <div class="nav nav-pills">
            <router-link class="text-center nav-link" :class="{ active : this.$route.name === 'All Articles' }" to="/articles">
                <i class="fas fa-stream"></i>
                <span class="ms-2">
                    Show Articles
                </span>
            </router-link>
            <router-link class="ms-2 text-center nav-link" :class="{ active : this.$route.name === 'New Article' }" to="/articles/new">
                <i class="fas fa-plus"></i>
                <span class="ms-2">
                    New Article
                </span>
            </router-link>
        </div>
    </nav>
    <div class="container">
        <router-view :key="$route.path"/>
    </div>
</template>
