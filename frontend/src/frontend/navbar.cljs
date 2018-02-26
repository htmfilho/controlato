(ns frontend.navbar)

(defn navbar []
  [:nav {:class "navbar .navbar-expand-md sticky-top navbar-dark bg-dark"} 
    [:a.navbar-brand {:href "#"} "Controlato"]
    [:button.navbar-toggler {:type "button" 
                             :data-toggle   "collapse" 
                             :data-target   "#navbarSupportedContent" 
                             :aria-controls "navbarSupportedContent" 
                             :aria-expanded "false" 
                             :aria-label    "Toggle navigation"}
      [:span.navbar-toggler-icon]]
    [:div {:class "collapse navbar-collapse" :id "navbarSupportedContent"}
      [:ul {:class "navbar-nav mr-auto"}
        [:li.nav-item [:a.nav-link {:href "#"} "Processes"]]
        [:li.nav-item [:a.nav-link {:href "#"} "Indicators"]]
        [:li {:class "nav-item dropdown"}
          [:a {:class         "nav-link dropdown-toggle"
               :href          "#"
               :id            "navbarDropdownMenuLink" 
               :data-toggle   "dropdown" 
               :aria-haspopup "true" 
               :aria-expanded "false"} "User Name"]
          [:div.dropdown-menu {:aria-labelledby "navbarDropdownMenuLink"}
            [:a.dropdown-item {:href "#"} "Profile"]
            [:a.dropdown-item {:href "#"} "Logout"]]]]]])
