def define_env(env):
    """
    This is the hook for the mkdocs-macros-plugin.
    """
    @env.macro
    def github_link(user, repo):
        url = f"https://github.com/{user}/{repo}"
        img = "![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white){ loading=lazy }"
        return f"[{img}]({url})" + "{ title='GitHub Repository' }"
    
    @env.macro
    def github_top_language(user, repo):
        url = f"https://img.shields.io/github/languages/top/{user}/{repo}"
        img = f"![GitHub top language]({url})"
        return img + "{ loading=lazy, title='Top Language' }"

    @env.macro
    def github_repo_licence(user, repo):
        url = f"https://img.shields.io/github/license/{user}/{repo}"
        img = f"![GitHub License]({url})"
        return img + "{ loading=lazy, title='License' }"