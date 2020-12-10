<template>
    <div>
        <router-link to="/articles">Articles</router-link> |
        <router-link to="/articles/new">New Article</router-link>
    </div>
    <router-view :key="$route.path"/>
</template>
