document.addEventListener("DOMContentLoaded", function () {
  function categories_update() {
    return document.querySelectorAll("[name=categories]:checked");
  }

  function institutions_update() {
    const categories = categories_update();
    const institutions_all = document.querySelectorAll("[name=organization]");
    institutions_all.forEach(function (i) {
      let i_div = i.parentElement.parentElement;
      i_div.hidden = false;
      categories.forEach(function (c) {
        if (i_div.dataset.categories.indexOf(c.value) < 0) {
          i_div.hidden = true;
        }
      });
    });
  }

  function summary_update() {
    let i_category_nodes = categories_update();
    let i_categories = [];
    i_category_nodes.forEach(function (i) {
      i_categories.push(String(i.value));
    });
    const i_bags = document.querySelector("[name=bags]").value;
    const i_organization = document.querySelector(
      "[name=organization]:checked",
    ).value;
    const i_address = document.querySelector("[name=address]").value;
    const i_city = document.querySelector("[name=city]").value;
    const i_postcode = document.querySelector("[name=postcode]").value;
    const i_phone = document.querySelector("[name=phone]").value;
    const i_date = document.querySelector("[name=date]").value;
    const i_time = document.querySelector("[name=time]").value;
    const i_info = document.querySelector("[name=more_info]").value;

    const s_donation = document.querySelector("#summary-donation");
    const s_organization = document.querySelector("#summary-organization");
    const s_address = document.querySelector("#summary-address");
    const s_city = document.querySelector("#summary-city");
    const s_postcode = document.querySelector("#summary-postcode");
    const s_phone = document.querySelector("#summary-phone");
    const s_date = document.querySelector("#summary-date");
    const s_time = document.querySelector("#summary-time");
    const s_info = document.querySelector("#summary-info");

    s_donation.innerText =
      "Liczba worków: " + i_bags + "; z kategorii: " + i_categories.join(", ");
    s_organization.innerText = "Adresat: " + i_organization;
    s_address.innerText = i_address;
    s_city.innerText = i_city;
    s_postcode.innerText = i_postcode;
    s_phone.innerText = i_phone;
    s_date.innerText = i_date;
    s_time.innerText = i_time;
    s_info.innerText = i_info;
  }

  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide =
        this.$buttonsContainer.querySelector(
          ".active",
        ).parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", (e) => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", (e) => {
        if (
          e.target.classList.contains("btn") &&
          e.target.parentElement.parentElement.classList.contains(
            "help--slides-pagination",
          )
        ) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach((btn) =>
        btn.firstElementChild.classList.remove("active"),
      );
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach((el) => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }

  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", (e) => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }

  document.querySelectorAll(".form-group--dropdown select").forEach((el) => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function (e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (
      tagName === "LI" &&
      target.parentElement.parentElement.classList.contains("dropdown")
    ) {
      return false;
    }

    if (
      tagName === "DIV" &&
      target.parentElement.classList.contains("dropdown")
    ) {
      return false;
    }

    document
      .querySelectorAll(".form-group--dropdown .dropdown")
      .forEach((el) => {
        el.classList.remove("selecting");
      });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(
        ".form--steps-instructions p",
      );
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.categories_selected = document.querySelectorAll(
        "[name=categories]:checked",
      );
      this.institution_selected = document.querySelectorAll(
        "[name=organization]:checked",
      );

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach((btn) => {
        btn.addEventListener("click", (e) => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach((btn) => {
        btn.addEventListener("click", (e) => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form
        .querySelector("form")
        .addEventListener("submit", (e) => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach((slide) => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden =
        this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
      this.categories_selected = document.querySelectorAll(
        "[name=categories]:checked",
      );
      this.institution_selected = document.querySelectorAll(
        "[name=organization]:checked",
      );

      institutions_update();
      summary_update();
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }

  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});
