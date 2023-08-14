from django.conf import settings

def vue_js_files(request):

    

        static_files_location = settings.STATIC_FILES_BASE_DIR
        vue_name = 'vue-prod' if settings.VUE_PROD else 'vue-dev'
        vue_dir = static_files_location / vue_name
        js_files = [x.relative_to(static_files_location) for x in vue_dir.glob("**/*.js")]
        css_files = [x.relative_to(static_files_location) for x in vue_dir.glob("**/*.css")]
        # "vue_js_paths": ["vue-dev\\assets\\index-e7ed6e49.js"]
        return {
                'vue_js_paths':js_files,
                'vue_css_paths':css_files,

        }
    