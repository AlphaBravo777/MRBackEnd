(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./src/$$_lazy_route_resource lazy recursive":
/*!**********************************************************!*\
  !*** ./src/$$_lazy_route_resource lazy namespace object ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error('Cannot find module "' + req + '".');
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _home_website_website_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./home/website/website.component */ "./src/app/home/website/website.component.ts");
/* harmony import */ var _home_shared_user_entry_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./home/shared/user-entry.component */ "./src/app/home/shared/user-entry.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var appRoutes = [
    {
        path: '',
        redirectTo: 'home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        component: _home_website_website_component__WEBPACK_IMPORTED_MODULE_2__["WebsiteComponent"]
    },
    {
        path: 'user',
        component: _home_shared_user_entry_component__WEBPACK_IMPORTED_MODULE_3__["UserEntryComponent"]
    },
];
var AppRoutingModule = /** @class */ (function () {
    function AppRoutingModule() {
    }
    AppRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forRoot(appRoutes, {
                    enableTracing: false,
                })
            ],
            exports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]
            ],
            providers: []
        })
    ], AppRoutingModule);
    return AppRoutingModule;
}());



/***/ }),

/***/ "./src/app/app.component.css":
/*!***********************************!*\
  !*** ./src/app/app.component.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/app.component.html":
/*!************************************!*\
  !*** ./src/app/app.component.html ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-home></app-home>\n"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var AppComponent = /** @class */ (function () {
    function AppComponent() {
    }
    AppComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! ./app.component.html */ "./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.css */ "./src/app/app.component.css")]
        })
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/platform-browser/animations */ "./node_modules/@angular/platform-browser/fesm5/animations.js");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _home_core_token_interceptor_service__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./home/core/token-interceptor.service */ "./src/app/home/core/token-interceptor.service.ts");
/* harmony import */ var _home_core_urls_service__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./home/core/urls.service */ "./src/app/home/core/urls.service.ts");
/* harmony import */ var _home_features_admin_auth_service__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./home/features/admin/auth.service */ "./src/app/home/features/admin/auth.service.ts");
/* harmony import */ var _home_features_admin_auth_guard__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./home/features/admin/auth.guard */ "./src/app/home/features/admin/auth.guard.ts");
/* harmony import */ var _home_website_website_module__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./home/website/website.module */ "./src/app/home/website/website.module.ts");
/* harmony import */ var _home_shared_user_entry_module__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./home/shared/user-entry.module */ "./src/app/home/shared/user-entry.module.ts");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ngx-permissions */ "./node_modules/ngx-permissions/ngx-permissions.umd.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(ngx_permissions__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _home_home_component__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./home/home.component */ "./src/app/home/home.component.ts");
/* harmony import */ var _home_website_website_component__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./home/website/website.component */ "./src/app/home/website/website.component.ts");
/* harmony import */ var _home_website_website_nav_website_nav_component__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./home/website/website-nav/website-nav.component */ "./src/app/home/website/website-nav/website-nav.component.ts");
/* harmony import */ var _home_shared_under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./home/shared/under-construction/under-construction.component */ "./src/app/home/shared/under-construction/under-construction.component.ts");
/* harmony import */ var _home_core_alerts_alert_component__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! ./home/core/alerts/alert.component */ "./src/app/home/core/alerts/alert.component.ts");
/* harmony import */ var _home_core_alerts_alert_service__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! ./home/core/alerts/alert.service */ "./src/app/home/core/alerts/alert.service.ts");
/* harmony import */ var _home_core_dialog_box_dialog_box_component__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! ./home/core/dialog-box/dialog-box.component */ "./src/app/home/core/dialog-box/dialog-box.component.ts");
/* harmony import */ var _node_modules_angular_material__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! ../../node_modules/@angular/material */ "./node_modules/@angular/material/esm5/material.es5.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};






















var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_5__["AppComponent"],
                _home_home_component__WEBPACK_IMPORTED_MODULE_14__["HomeComponent"],
                _home_website_website_component__WEBPACK_IMPORTED_MODULE_15__["WebsiteComponent"],
                _home_website_website_nav_website_nav_component__WEBPACK_IMPORTED_MODULE_16__["WebsiteNavComponent"],
                _home_shared_under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_17__["UnderConstructionComponent"],
                _home_core_alerts_alert_component__WEBPACK_IMPORTED_MODULE_18__["AlertComponent"],
                _home_core_dialog_box_dialog_box_component__WEBPACK_IMPORTED_MODULE_20__["DialogBoxComponent"],
            ],
            imports: [
                _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_4__["BrowserAnimationsModule"],
                _node_modules_angular_material__WEBPACK_IMPORTED_MODULE_21__["MatDialogModule"],
                _home_website_website_module__WEBPACK_IMPORTED_MODULE_11__["WebsiteModule"],
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormsModule"],
                _app_routing_module__WEBPACK_IMPORTED_MODULE_6__["AppRoutingModule"],
                _angular_common_http__WEBPACK_IMPORTED_MODULE_3__["HttpClientModule"],
                _home_shared_user_entry_module__WEBPACK_IMPORTED_MODULE_12__["UserEntryModule"],
                ngx_permissions__WEBPACK_IMPORTED_MODULE_13__["NgxPermissionsModule"].forRoot(),
            ],
            providers: [
                _home_features_admin_auth_guard__WEBPACK_IMPORTED_MODULE_10__["AuthGuard"],
                _home_features_admin_auth_service__WEBPACK_IMPORTED_MODULE_9__["AuthService"],
                _home_core_urls_service__WEBPACK_IMPORTED_MODULE_8__["UrlsService"],
                _home_core_alerts_alert_service__WEBPACK_IMPORTED_MODULE_19__["AlertService"],
                {
                    provide: _angular_common_http__WEBPACK_IMPORTED_MODULE_3__["HTTP_INTERCEPTORS"],
                    useClass: _home_core_token_interceptor_service__WEBPACK_IMPORTED_MODULE_7__["TokenInterceptorService"],
                    multi: true
                }
            ],
            entryComponents: [
                _home_core_dialog_box_dialog_box_component__WEBPACK_IMPORTED_MODULE_20__["DialogBoxComponent"],
            ],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_5__["AppComponent"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/app/home/core/alerts/alert.component.css":
/*!******************************************************!*\
  !*** ./src/app/home/core/alerts/alert.component.css ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".alert{\r\n    background-color: #fff;\r\n    margin: 10px;\r\n    padding: 10px;\r\n}\r\n\r\n.alert-success{\r\n    color: #008000;\r\n}\r\n\r\n.alert-danger{\r\n    color: #ff1117;\r\n}\r\n\r\n"

/***/ }),

/***/ "./src/app/home/core/alerts/alert.component.html":
/*!*******************************************************!*\
  !*** ./src/app/home/core/alerts/alert.component.html ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div *ngIf=\"message\" [ngClass]=\"{ 'alert': message, 'alert-success': message.type === 'success', 'alert-danger': message.type === 'error' }\">{{message.text}}</div>"

/***/ }),

/***/ "./src/app/home/core/alerts/alert.component.ts":
/*!*****************************************************!*\
  !*** ./src/app/home/core/alerts/alert.component.ts ***!
  \*****************************************************/
/*! exports provided: AlertComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AlertComponent", function() { return AlertComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _alert_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./alert.service */ "./src/app/home/core/alerts/alert.service.ts");
// The alert component passes alert messages to the template whenever a message is received from the alert service.
// It does this by subscribing to the alert service's getMessage() method which returns an Observable.
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var AlertComponent = /** @class */ (function () {
    function AlertComponent(alertService) {
        this.alertService = alertService;
    }
    AlertComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.subscription = this.alertService.getMessage().subscribe(function (message) {
            if (!message) {
                return;
            }
            _this.message = message;
            console.log('===', message);
        });
    };
    AlertComponent.prototype.ngOnDestroy = function () {
        this.subscription.unsubscribe();
    };
    AlertComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-auth-alert',
            template: __webpack_require__(/*! ./alert.component.html */ "./src/app/home/core/alerts/alert.component.html"),
            styles: [__webpack_require__(/*! ./alert.component.css */ "./src/app/home/core/alerts/alert.component.css")]
        }),
        __metadata("design:paramtypes", [_alert_service__WEBPACK_IMPORTED_MODULE_1__["AlertService"]])
    ], AlertComponent);
    return AlertComponent;
}());



/***/ }),

/***/ "./src/app/home/core/alerts/alert.service.ts":
/*!***************************************************!*\
  !*** ./src/app/home/core/alerts/alert.service.ts ***!
  \***************************************************/
/*! exports provided: AlertService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AlertService", function() { return AlertService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm5/index.js");
// The alert service enables any component in the application to display alert messages at the top of the page via the alert component.
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
// It has methods for displaying success and error messages, and a getMessage() method that returns an Observable that is used by the
// alert component to subscribe to notifications for whenever a message should be displayed.



var AlertService = /** @class */ (function () {
    function AlertService(router) {
        var _this = this;
        this.router = router;
        this.subject = new rxjs__WEBPACK_IMPORTED_MODULE_2__["Subject"]();
        this.keepAfterNavigationChange = false;
        // clear alert message on route change
        router.events.subscribe(function (event) {
            if (event instanceof _angular_router__WEBPACK_IMPORTED_MODULE_1__["NavigationStart"]) {
                if (_this.keepAfterNavigationChange) {
                    // only keep for a single location change
                    _this.keepAfterNavigationChange = false;
                }
                else {
                    // clear alert
                    _this.subject.next();
                }
            }
        });
    }
    AlertService.prototype.success = function (message, keepAfterNavigationChange) {
        if (keepAfterNavigationChange === void 0) { keepAfterNavigationChange = false; }
        this.keepAfterNavigationChange = keepAfterNavigationChange;
        this.subject.next({ type: 'success', text: message });
    };
    AlertService.prototype.error = function (message, keepAfterNavigationChange) {
        if (keepAfterNavigationChange === void 0) { keepAfterNavigationChange = false; }
        this.keepAfterNavigationChange = keepAfterNavigationChange;
        this.subject.next({ type: 'error', text: message });
    };
    AlertService.prototype.getMessage = function () {
        return this.subject.asObservable();
    };
    AlertService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])(),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], AlertService);
    return AlertService;
}());



/***/ }),

/***/ "./src/app/home/core/dialog-box/dialog-box.component.css":
/*!***************************************************************!*\
  !*** ./src/app/home/core/dialog-box/dialog-box.component.css ***!
  \***************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".wrapper {\r\n    width: auto;\r\n}"

/***/ }),

/***/ "./src/app/home/core/dialog-box/dialog-box.component.html":
/*!****************************************************************!*\
  !*** ./src/app/home/core/dialog-box/dialog-box.component.html ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div *ngIf='dialogtype === \"confirmMessage\"'>\n    <div class=\"wrapper\">\n        <h1 mat-dialog-title>Confirm</h1>\n        <div mat-dialog-content>{{confirmMessage}}</div>\n        <div mat-dialog-actions>\n            <button md-button (click)=\"dialogRef.close(false)\">I will try again</button>\n        </div>\n    </div>\n</div>\n\n<div *ngIf='dialogtype === \"stockCleared\"'>\n    <div class=\"wrapper\">\n        <h1 mat-dialog-title>Stock Cleared</h1>\n        <div mat-dialog-content>{{confirmMessage}}</div>\n        <div mat-dialog-actions>\n            <button md-button (click)=\"dialogRef.close(false)\">OK</button>\n        </div>\n    </div>\n</div>"

/***/ }),

/***/ "./src/app/home/core/dialog-box/dialog-box.component.ts":
/*!**************************************************************!*\
  !*** ./src/app/home/core/dialog-box/dialog-box.component.ts ***!
  \**************************************************************/
/*! exports provided: DialogBoxComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DialogBoxComponent", function() { return DialogBoxComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/material */ "./node_modules/@angular/material/esm5/material.es5.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var DialogBoxComponent = /** @class */ (function () {
    function DialogBoxComponent(dialogRef) {
        this.dialogRef = dialogRef;
    }
    DialogBoxComponent.prototype.ngOnInit = function () {
    };
    DialogBoxComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-dialog-box',
            template: __webpack_require__(/*! ./dialog-box.component.html */ "./src/app/home/core/dialog-box/dialog-box.component.html"),
            styles: [__webpack_require__(/*! ./dialog-box.component.css */ "./src/app/home/core/dialog-box/dialog-box.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_material__WEBPACK_IMPORTED_MODULE_1__["MatDialogRef"]])
    ], DialogBoxComponent);
    return DialogBoxComponent;
}());



/***/ }),

/***/ "./src/app/home/core/dialog-box/dialog-box.service.ts":
/*!************************************************************!*\
  !*** ./src/app/home/core/dialog-box/dialog-box.service.ts ***!
  \************************************************************/
/*! exports provided: DialogBoxService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DialogBoxService", function() { return DialogBoxService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _node_modules_angular_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../../../node_modules/@angular/material */ "./node_modules/@angular/material/esm5/material.es5.js");
/* harmony import */ var _dialog_box_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./dialog-box.component */ "./src/app/home/core/dialog-box/dialog-box.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var DialogBoxService = /** @class */ (function () {
    function DialogBoxService(dialog) {
        this.dialog = dialog;
    }
    DialogBoxService.prototype.openConfirmationDialog = function () {
        var _this = this;
        this.dialogRef = this.dialog.open(_dialog_box_component__WEBPACK_IMPORTED_MODULE_2__["DialogBoxComponent"], {
            panelClass: 'my-centered-dialog',
            disableClose: false
        });
        this.dialogRef.componentInstance.confirmMessage = 'The stock did not safe correctly, check connection and try again!';
        this.dialogRef.componentInstance.dialogtype = 'confirmMessage';
        this.dialogRef.afterClosed().subscribe(function (result) {
            if (result) {
                // do confirmation actions
            }
            _this.dialogRef = null;
        });
    };
    DialogBoxService.prototype.openStockClearedDialog = function () {
        var _this = this;
        this.dialogRef = this.dialog.open(_dialog_box_component__WEBPACK_IMPORTED_MODULE_2__["DialogBoxComponent"], {
            panelClass: 'my-centered-dialog',
            disableClose: false
        });
        this.dialogRef.componentInstance.confirmMessage = 'The stock have been cleared';
        this.dialogRef.componentInstance.dialogtype = 'stockCleared';
        this.dialogRef.afterClosed().subscribe(function (result) {
            if (result) {
                // do confirmation actions
            }
            _this.dialogRef = null;
        });
    };
    DialogBoxService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_node_modules_angular_material__WEBPACK_IMPORTED_MODULE_1__["MatDialog"]])
    ], DialogBoxService);
    return DialogBoxService;
}());



/***/ }),

/***/ "./src/app/home/core/token-interceptor.service.ts":
/*!********************************************************!*\
  !*** ./src/app/home/core/token-interceptor.service.ts ***!
  \********************************************************/
/*! exports provided: TokenInterceptorService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TokenInterceptorService", function() { return TokenInterceptorService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _features_admin_auth_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../features/admin/auth.service */ "./src/app/home/features/admin/auth.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var TokenInterceptorService = /** @class */ (function () {
    function TokenInterceptorService(_auth) {
        this._auth = _auth;
    }
    // Here we intercept ANY HTTP request, and we return an observable that I think the next handler can intercept if neccesary
    TokenInterceptorService.prototype.intercept = function (request, next) {
        // Here we get the token in browser storage, and in the next line check if there is a token or not.
        var hasToken = this._auth.getToken();
        if (hasToken) {
            // Initial request in imutable, so we have to clone it first
            request = request.clone({
                // Now we are setting the actual header
                setHeaders: {
                    Authorization: "JWT " + this._auth.getToken()
                }
            });
        }
        else {
            console.log('There is no token');
        }
        // We now return the request, and if there is another interceptor it will pick it up, or it will be send through
        return next.handle(request);
    };
    TokenInterceptorService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_features_admin_auth_service__WEBPACK_IMPORTED_MODULE_1__["AuthService"]])
    ], TokenInterceptorService);
    return TokenInterceptorService;
}());

/*

import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add authorization header with jwt token if available
        const currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            request = request.clone({
                setHeaders: {
                    Authorization: `Bearer ${currentUser.token}`
                }
            });
        }

        return next.handle(request);
    }
}
*/


/***/ }),

/***/ "./src/app/home/core/urls.service.ts":
/*!*******************************************!*\
  !*** ./src/app/home/core/urls.service.ts ***!
  \*******************************************/
/*! exports provided: UrlsService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UrlsService", function() { return UrlsService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var UrlsService = /** @class */ (function () {
    function UrlsService() {
        this.rootUrl = 'http://192.168.45.2:8000/';
    }
    UrlsService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [])
    ], UrlsService);
    return UrlsService;
}());



/***/ }),

/***/ "./src/app/home/features/admin/auth.guard.ts":
/*!***************************************************!*\
  !*** ./src/app/home/features/admin/auth.guard.ts ***!
  \***************************************************/
/*! exports provided: AuthGuard */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AuthGuard", function() { return AuthGuard; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _auth_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./auth.service */ "./src/app/home/features/admin/auth.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var AuthGuard = /** @class */ (function () {
    function AuthGuard(_auth, _router) {
        this._auth = _auth;
        this._router = _router;
    }
    AuthGuard.prototype.canActivate = function () {
        if (this._auth.loggedIn()) {
            return true;
        }
        else {
            this._router.navigate(['home']);
            return false;
        }
    };
    AuthGuard = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_auth_service__WEBPACK_IMPORTED_MODULE_2__["AuthService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], AuthGuard);
    return AuthGuard;
}());



/***/ }),

/***/ "./src/app/home/features/admin/auth.service.ts":
/*!*****************************************************!*\
  !*** ./src/app/home/features/admin/auth.service.ts ***!
  \*****************************************************/
/*! exports provided: AuthService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AuthService", function() { return AuthService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _core_urls_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../core/urls.service */ "./src/app/home/core/urls.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var AuthService = /** @class */ (function () {
    function AuthService(http, _urlService) {
        this.http = http;
        this._urlService = _urlService;
        this._loginUrl = this._urlService.rootUrl + 'api/rest-auth/login/';
        this._registerUrl = this._urlService.rootUrl + 'api/rest-auth/registration/';
    }
    AuthService.prototype.registerUser = function (user) {
        return this.http.post(this._registerUrl, user);
    };
    AuthService.prototype.loginUser = function (user) {
        return this.http.post(this._loginUrl, user);
    };
    AuthService.prototype.loggedIn = function () {
        return !!localStorage.getItem('token');
    };
    AuthService.prototype.getToken = function () {
        return localStorage.getItem('token');
    };
    AuthService.prototype.logout = function () {
        // remove user from local storage to log user out
        localStorage.removeItem('token');
        // localStorage.clear();
    };
    AuthService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"], _core_urls_service__WEBPACK_IMPORTED_MODULE_2__["UrlsService"]])
    ], AuthService);
    return AuthService;
}());

// TODO: See if you must not change this server adress, or add a variable for it, to make the app in phone work


/***/ }),

/***/ "./src/app/home/features/admin/login/login.component.css":
/*!***************************************************************!*\
  !*** ./src/app/home/features/admin/login/login.component.css ***!
  \***************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\n\r\n.login-page {\r\n  width: 80%;\r\n  padding: 3% 0 0;\r\n  margin: auto;\r\n}\r\n.form {\r\n  position: relative;\r\n  z-index: 1;\r\n  background: #FFFFFF;\r\n  max-width: 360px;\r\n  margin: 0 auto 100px;\r\n  padding: 20px;\r\n  text-align: center;\r\n  /*box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);*/\r\n}\r\n.form input {\r\n  font-family: Arial, Helvetica, sans-serif;\r\n  outline: 0;\r\n  background: #f2f2f2;\r\n  width: 100%;\r\n  border: 0;\r\n  margin: 0 0 15px;\r\n  padding: 15px;\r\n  box-sizing: border-box;\r\n  font-size: 14px;\r\n}\r\n.form button {\r\n  font-family: Arial, Helvetica, sans-serif;\r\n  text-transform: uppercase;\r\n  outline: 0;\r\n  background: rgb(172, 22, 47);\r\n  width: 100%;\r\n  border: 0;\r\n  padding: 15px;\r\n  color: #FFFFFF;\r\n  font-size: 14px;\r\n  transition: all 0.3 ease;\r\n  cursor: pointer;\r\n}\r\n.form button:hover,.form button:active,.form button:focus {\r\n  background: rgb(172, 22, 47);\r\n}\r\n.form .message {\r\n  margin: 15px 0 0;\r\n  color: #b3b3b3;\r\n  font-size: 12px;\r\n}\r\n.form .message a {\r\n  color: rgb(172, 22, 47);\r\n  text-decoration: none;\r\n}\r\n.form .register-form {\r\n  display: none;\r\n}\r\n.container {\r\n  position: relative;\r\n  z-index: 1;\r\n  max-width: 300px;\r\n  margin: 0 auto;\r\n}\r\n.container:before, .container:after {\r\n  content: \"\";\r\n  display: block;\r\n  clear: both;\r\n}\r\n.container .info {\r\n  margin: 50px auto;\r\n  text-align: center;\r\n}\r\n.container .info h1 {\r\n  margin: 0 0 15px;\r\n  padding: 0;\r\n  font-size: 36px;\r\n  font-weight: 300;\r\n  color: #1a1a1a;\r\n}\r\n.container .info span {\r\n  color: #4d4d4d;\r\n  font-size: 12px;\r\n}\r\n.container .info span a {\r\n  color: #000000;\r\n  text-decoration: none;\r\n}\r\n.container .info span .fa {\r\n  color: #EF3B3A;\r\n}\r\nbody {\r\n  background: rgb(172, 22, 47); /* fallback for old browsers */\r\n  background: linear-gradient(to left, #76b852, #8DC26F);\r\n  font-family: Arial, Helvetica, sans-serif;\r\n  -webkit-font-smoothing: antialiased;\r\n  -moz-osx-font-smoothing: grayscale;      \r\n}"

/***/ }),

/***/ "./src/app/home/features/admin/login/login.component.html":
/*!****************************************************************!*\
  !*** ./src/app/home/features/admin/login/login.component.html ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"login-page\">\n  <div class=\"form\">\n    <form class=\"login-form\">\n      <input [(ngModel)]=\"loginUserData.username\" name=\"username\" type=\"text\" placeholder=\"username\"/>\n      <input [(ngModel)]=\"loginUserData.password\" name=\"password\" type=\"password\" placeholder=\"password\"/>\n      <button (click)=\"loginUser()\">login</button>\n    </form>\n  </div>\n</div>\n\n"

/***/ }),

/***/ "./src/app/home/features/admin/login/login.component.ts":
/*!**************************************************************!*\
  !*** ./src/app/home/features/admin/login/login.component.ts ***!
  \**************************************************************/
/*! exports provided: LoginComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "LoginComponent", function() { return LoginComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _auth_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../auth.service */ "./src/app/home/features/admin/auth.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var LoginComponent = /** @class */ (function () {
    function LoginComponent(_auth, _router) {
        this._auth = _auth;
        this._router = _router;
        this.loginUserData = { username: '', password: '' };
    }
    LoginComponent.prototype.ngOnInit = function () {
        this._auth.logout();
    };
    LoginComponent.prototype.loginUser = function () {
        var _this = this;
        this._auth.loginUser(this.loginUserData)
            .subscribe(function (res) {
            console.log(res);
            localStorage.setItem('token', res.token);
            localStorage.setItem('userID', res.user.pk);
            _this._router.navigate(['user/user-nav/']);
        }, function (err) { return console.log(err); });
        console.log(this.loginUserData);
    };
    LoginComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-login',
            template: __webpack_require__(/*! ./login.component.html */ "./src/app/home/features/admin/login/login.component.html"),
            styles: [__webpack_require__(/*! ./login.component.css */ "./src/app/home/features/admin/login/login.component.css")]
        }),
        __metadata("design:paramtypes", [_auth_service__WEBPACK_IMPORTED_MODULE_1__["AuthService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"]])
    ], LoginComponent);
    return LoginComponent;
}());



/***/ }),

/***/ "./src/app/home/features/admin/register-user/register.component.css":
/*!**************************************************************************!*\
  !*** ./src/app/home/features/admin/register-user/register.component.css ***!
  \**************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\n\r\n.login-page {\r\n    width: 80%;\r\n    padding: 3% 0 0;\r\n    margin: auto;\r\n  }\r\n  .form {\r\n    position: relative;\r\n    z-index: 1;\r\n    background: #FFFFFF;\r\n    max-width: 360px;\r\n    margin: 0 auto 100px;\r\n    padding: 20px;\r\n    text-align: center;\r\n    /*box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);*/\r\n  }\r\n  .form input {\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    outline: 0;\r\n    background: #f2f2f2;\r\n    width: 100%;\r\n    border: 0;  \r\n    margin: 0 0 15px;\r\n    padding: 15px;\r\n    box-sizing: border-box;\r\n    font-size: 14px;\r\n  }\r\n  .form button {\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    text-transform: uppercase;\r\n    outline: 0;\r\n    background: rgb(172, 22, 47);\r\n    width: 100%;\r\n    border: 0;\r\n    padding: 15px;\r\n    color: #FFFFFF;\r\n    font-size: 14px;\r\n    transition: all 0.3 ease;\r\n    cursor: pointer;\r\n  }\r\n  .form button:hover,.form button:active,.form button:focus {\r\n    background: rgb(172, 22, 47);\r\n  }\r\n  .form .message {\r\n    margin: 15px 0 0;\r\n    color: #b3b3b3;\r\n    font-size: 12px;\r\n  }\r\n  .form .message a {\r\n    color: rgb(172, 22, 47);\r\n    text-decoration: none;\r\n  }\r\n  .container {\r\n    position: relative;\r\n    z-index: 1;\r\n    max-width: 300px;\r\n    margin: 0 auto;\r\n  }\r\n  .container:before, .container:after {\r\n    content: \"\";\r\n    display: block;\r\n    clear: both;\r\n  }\r\n  .container .info {\r\n    margin: 50px auto;\r\n    text-align: center;\r\n  }\r\n  .container .info h1 {\r\n    margin: 0 0 15px;\r\n    padding: 0;\r\n    font-size: 36px;\r\n    font-weight: 300;\r\n    color: #1a1a1a;\r\n  }\r\n  .container .info span {\r\n    color: #4d4d4d;\r\n    font-size: 12px;\r\n  }\r\n  .container .info span a {\r\n    color: #000000;\r\n    text-decoration: none;\r\n  }\r\n  .container .info span .fa {\r\n    color: #EF3B3A;\r\n  }\r\n  body {\r\n    background: rgb(172, 22, 47); /* fallback for old browsers */\r\n    background: linear-gradient(to left, #76b852, #8DC26F);\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    -webkit-font-smoothing: antialiased;\r\n    -moz-osx-font-smoothing: grayscale;      \r\n  }"

/***/ }),

/***/ "./src/app/home/features/admin/register-user/register.component.html":
/*!***************************************************************************!*\
  !*** ./src/app/home/features/admin/register-user/register.component.html ***!
  \***************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<!-- <div class=\"login-page\">\n  <div class=\"form\">\n    <form class=\"register-form\">\n      <input [(ngModel)]=\"registerUserData.username\" name=\"username\" type=\"text\" placeholder=\"username\"/>\n      <input [(ngModel)]=\"registerUserData.password1\" name=\"password1\" type=\"password\" placeholder=\"password\"/>\n      <input [(ngModel)]=\"registerUserData.password2\" name=\"password2\" type=\"password\" placeholder=\"confirm password\"/>\n      <input [(ngModel)]=\"registerUserData.email\" name=\"email\" type=\"text\" placeholder=\"email address\"/>\n      <button (click)=\"registerUser()\">create</button>\n      <p class=\"message\">Already registered? <a href=\"login\">Login</a></p>\n    </form>\n  </div>\n</div> -->"

/***/ }),

/***/ "./src/app/home/features/admin/register-user/register.component.ts":
/*!*************************************************************************!*\
  !*** ./src/app/home/features/admin/register-user/register.component.ts ***!
  \*************************************************************************/
/*! exports provided: RegisterComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RegisterComponent", function() { return RegisterComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _auth_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../auth.service */ "./src/app/home/features/admin/auth.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var RegisterComponent = /** @class */ (function () {
    function RegisterComponent(auth, router) {
        this.auth = auth;
        this.router = router;
        this.registerUserData = { username: '', password: '', password2: '', email: '' };
    }
    RegisterComponent.prototype.ngOnInit = function () {
    };
    RegisterComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-register',
            template: __webpack_require__(/*! ./register.component.html */ "./src/app/home/features/admin/register-user/register.component.html"),
            styles: [__webpack_require__(/*! ./register.component.css */ "./src/app/home/features/admin/register-user/register.component.css")]
        }),
        __metadata("design:paramtypes", [_auth_service__WEBPACK_IMPORTED_MODULE_2__["AuthService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], RegisterComponent);
    return RegisterComponent;
}());



/***/ }),

/***/ "./src/app/home/features/factory/factory-routing.module.ts":
/*!*****************************************************************!*\
  !*** ./src/app/home/features/factory/factory-routing.module.ts ***!
  \*****************************************************************/
/*! exports provided: FactoryRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FactoryRoutingModule", function() { return FactoryRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};


var appRoutes = [];
//     {
//         path: 'roles', component: FactoryComponent
//     },
//     {
//         path: 'permissions', component: FactoryComponent
//
//     },
//     {
//         path: 'no-roles',
//         component: FactoryComponent,
//         canActivate: [NgxPermissionsGuard],
//         data: {
//             permissions: {
//                 only: 'Nice'
//             }
//         }
//     },
//     {
//         path: 'no-permissions',
//         component: FactoryComponent,
//         canActivate: [NgxPermissionsGuard],
//         data: {
//             permissions: {
//                 only: 'Nice'
//             }
//         }
//     },
// ];
var FactoryRoutingModule = /** @class */ (function () {
    function FactoryRoutingModule() {
    }
    FactoryRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forChild(appRoutes)
            ],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]]
        })
    ], FactoryRoutingModule);
    return FactoryRoutingModule;
}());



/***/ }),

/***/ "./src/app/home/features/factory/factory.component.css":
/*!*************************************************************!*\
  !*** ./src/app/home/features/factory/factory.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/features/factory/factory.component.html":
/*!**************************************************************!*\
  !*** ./src/app/home/features/factory/factory.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div *ngxPermissionsOnly=\"['floor-supervisor', 'Lshape-leader', 'shift-supervisor']\">\n  <div>You can see this text congrats</div>\n  <a class='buttonMenus' routerLink=\"/user-nav\" routerLinkActive=\"active\">ADMIN</a>\n</div>\n\n<ng-template ngxPermissionsOnly=\"shift-supervisor\">\n  <nav>\n    <a class='buttonMenus' routerLink=\"/user-nav\" routerLinkActive=\"active\">ADMIN</a>\n  </nav>\n</ng-template>\n\n<ng-template [ngxPermissionsExcept]=\"['JOHNY']\">\n  <nav>\n    <a class='buttonMenus' routerLink=\"/user-nav\" routerLinkActive=\"active\">NOT JOHNY</a>\n  </nav>\n</ng-template>\n\n\n<!--\n\n<router-outlet name='factoryNav'></router-outlet>   \n\n<div class=\"center-screen\">\n  <nav>\n    <a class='buttonMenus' routerLink=\"/user-nav\" routerLinkActive=\"active\">Stock1</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'factoryNav': ['stocks']}} ]\">Stock</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'factoryNav': ['high-risk']}} ]\">Hi-Risk</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'factoryNav': ['user-nav']}} ]\">Production</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">L-Shape</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">Storage</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">Receiving</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">Factory Office</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">Workshop</a>\n    <a class='buttonMenus' [routerLink]=\"[{outlets: {'websiteNav': ['stocks']}} ]\">Food safety</a>\n  </nav>\n</div>\n\n -->"

/***/ }),

/***/ "./src/app/home/features/factory/factory.component.ts":
/*!************************************************************!*\
  !*** ./src/app/home/features/factory/factory.component.ts ***!
  \************************************************************/
/*! exports provided: FactoryComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FactoryComponent", function() { return FactoryComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ngx-permissions */ "./node_modules/ngx-permissions/ngx-permissions.umd.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(ngx_permissions__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _core_urls_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../core/urls.service */ "./src/app/home/core/urls.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var FactoryComponent = /** @class */ (function () {
    function FactoryComponent(permissionsService, http, _urlService) {
        this.permissionsService = permissionsService;
        this.http = http;
        this._urlService = _urlService;
        this.test = this._urlService.rootUrl + 'api/test/';
        this.data = [];
    }
    FactoryComponent.prototype.ngOnInit = function () {
        // const perm = ['EDITOR'];
        var _this = this;
        // this.permissionsService.loadPermissions(perm);
        this.http.get(this.test).subscribe(function (groups) {
            for (var _i = 0, _a = Object.keys(groups.groups); _i < _a.length; _i++) {
                var key = _a[_i];
                // console.log(this.data[0][key].name);
                _this.data.push(groups.groups[key].name);
            }
            _this.permissionsService.loadPermissions(_this.data);
            console.log(_this.data);
        });
        // this.http.get('url').subscribe((permissions) => {
        //    // const perm = ["ADMIN", "EDITOR"]; example of permissions
        //    this.permissionsService.loadPermissions(permissions);
        // });
    };
    FactoryComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-factory',
            template: __webpack_require__(/*! ./factory.component.html */ "./src/app/home/features/factory/factory.component.html"),
            styles: [__webpack_require__(/*! ./factory.component.css */ "./src/app/home/features/factory/factory.component.css")]
        }),
        __metadata("design:paramtypes", [ngx_permissions__WEBPACK_IMPORTED_MODULE_1__["NgxPermissionsService"],
            _angular_common_http__WEBPACK_IMPORTED_MODULE_2__["HttpClient"],
            _core_urls_service__WEBPACK_IMPORTED_MODULE_3__["UrlsService"]])
    ], FactoryComponent);
    return FactoryComponent;
}());



/***/ }),

/***/ "./src/app/home/features/factory/factory.module.ts":
/*!*********************************************************!*\
  !*** ./src/app/home/features/factory/factory.module.ts ***!
  \*********************************************************/
/*! exports provided: FactoryModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FactoryModule", function() { return FactoryModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ngx-permissions */ "./node_modules/ngx-permissions/ngx-permissions.umd.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(ngx_permissions__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _factory_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./factory-routing.module */ "./src/app/home/features/factory/factory-routing.module.ts");
/* harmony import */ var _factory_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./factory.component */ "./src/app/home/features/factory/factory.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};





var FactoryModule = /** @class */ (function () {
    function FactoryModule() {
    }
    FactoryModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                _factory_routing_module__WEBPACK_IMPORTED_MODULE_3__["FactoryRoutingModule"],
                ngx_permissions__WEBPACK_IMPORTED_MODULE_2__["NgxPermissionsModule"].forChild()
            ],
            declarations: [_factory_component__WEBPACK_IMPORTED_MODULE_4__["FactoryComponent"]]
        })
    ], FactoryModule);
    return FactoryModule;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/get-products.component.css":
/*!***************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/get-products.component.css ***!
  \***************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/get-products.component.html":
/*!****************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/get-products.component.html ***!
  \****************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-stock-products *ngIf='processedStockMain'\r\n[productNames]=\"productNames\" \r\n[processedStockMain]=\"processedStockMain\"\r\n[stocktime]=\"stocktime\">\r\n</app-stock-products>"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/get-products.component.ts":
/*!**************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/get-products.component.ts ***!
  \**************************************************************************************/
/*! exports provided: GetProductsComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "GetProductsComponent", function() { return GetProductsComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _core_dialog_box_dialog_box_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../../core/dialog-box/dialog-box.service */ "./src/app/home/core/dialog-box/dialog-box.service.ts");
/* harmony import */ var _stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../stock-services/processed-stock.service */ "./src/app/home/features/stock/stock-services/processed-stock.service.ts");
/* harmony import */ var _stock_services_stock_api_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../stock-services/stock-api.service */ "./src/app/home/features/stock/stock-services/stock-api.service.ts");
/* harmony import */ var _node_modules_angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../../../../../../node_modules/@angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};





// https://stackoverflow.com/questions/32575695/disable-chrome-auto-reload-on-time-out-error/32718801#32718801
// http://devarea.com/building-a-simple-website-with-angular-4-and-django-and-deploy-it-to-heroku/
// https://medium.com/@nicholaskajoh/heres-a-dead-simple-react-django-setup-for-your-next-project-c0b0036663c6
// https://octaviancorlade.github.io/django-angular5-web-app-building/
// connecting angular and django app
var GetProductsComponent = /** @class */ (function () {
    function GetProductsComponent(dialogBoxService, processedStockService, stockAPI, route) {
        var _this = this;
        this.dialogBoxService = dialogBoxService;
        this.processedStockService = processedStockService;
        this.stockAPI = stockAPI;
        this.route = route;
        this.route.params.subscribe(function (params) {
            return _this.stocktime = params['time'];
        });
    }
    GetProductsComponent.prototype.ngOnInit = function () {
        console.log(this.stocktime);
        this.getProcessedStockMain();
    };
    GetProductsComponent.prototype.getProcessedStockMain = function () {
        var _this = this;
        this.stockAPI.getProductContainers()
            .subscribe(function (prodContainers) {
            _this.getProductsAndContainers(prodContainers);
        });
    };
    GetProductsComponent.prototype.getProductsAndContainers = function (prodContainers) {
        var _this = this;
        var emptyProdConGroup = [];
        this.stockAPI.getProducts()
            .subscribe(function (products) {
            _this.productNames = products;
            emptyProdConGroup = _this.createGroupWithProducts(products);
            _this.processedStockMain = _this.insertContainers(emptyProdConGroup, prodContainers);
            _this.addAmountsToStockMain(_this.processedStockMain);
        });
    };
    GetProductsComponent.prototype.createGroupWithProducts = function (products) {
        var emptyProdConGroup = [];
        for (var prodnum = 0; prodnum < products.length; ++prodnum) {
            var emptyProdCon = { product: products[prodnum].productid, mainContainer: [] };
            emptyProdConGroup.push(emptyProdCon);
        }
        return emptyProdConGroup;
    };
    GetProductsComponent.prototype.insertContainers = function (fullProdConGroup, containers) {
        for (var connum = 0; connum < containers.length; ++connum) {
            for (var prodgroup = 0; prodgroup < fullProdConGroup.length; ++prodgroup) {
                if (fullProdConGroup[prodgroup].product === containers[connum].productid) {
                    var con = { container: containers[connum].container, amount: [] };
                    fullProdConGroup[prodgroup].mainContainer.push(con);
                }
            }
        }
        return fullProdConGroup;
    };
    GetProductsComponent.prototype.addAmountsToStockMain = function (processedStockMain) {
        var _this = this;
        this.stockAPI.getTimedStock(this.stocktime)
            .subscribe(function (stock) {
            _this.grantTotal = _this.getGrandTotal(stock, processedStockMain);
            // console.log(this.grantTotal);
            _this.processedStockMain = _this.grantTotal;
            localStorage.setItem('stock', JSON.stringify(processedStockMain));
        });
    };
    GetProductsComponent.prototype.getGrandTotal = function (stock, processedStockMain) {
        for (var stk = 0; stk < stock.length; ++stk) {
            for (var main = 0; main < processedStockMain.length; ++main) {
                if (stock[stk].name === processedStockMain[main].product) {
                    for (var con = 0; con < processedStockMain[main].mainContainer.length; ++con) {
                        if (stock[stk].container === processedStockMain[main].mainContainer[con].container) {
                            processedStockMain[main].mainContainer[con].amount.push(stock[stk].amount);
                        }
                    }
                }
            }
        }
        return processedStockMain;
    };
    GetProductsComponent.prototype.ngOnDestroy = function () {
        // this.dialogBoxService.openConfirmationDialog();
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", String)
    ], GetProductsComponent.prototype, "stocktime", void 0);
    GetProductsComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-get-products',
            template: __webpack_require__(/*! ./get-products.component.html */ "./src/app/home/features/stock/processed/get-products/get-products.component.html"),
            styles: [__webpack_require__(/*! ./get-products.component.css */ "./src/app/home/features/stock/processed/get-products/get-products.component.css")]
        }),
        __metadata("design:paramtypes", [_core_dialog_box_dialog_box_service__WEBPACK_IMPORTED_MODULE_1__["DialogBoxService"],
            _stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_2__["ProcessedStockService"],
            _stock_services_stock_api_service__WEBPACK_IMPORTED_MODULE_3__["StockAPIService"],
            _node_modules_angular_router__WEBPACK_IMPORTED_MODULE_4__["ActivatedRoute"]])
    ], GetProductsComponent);
    return GetProductsComponent;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.css":
/*!********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.css ***!
  \********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "body{ \r\n    background:url(http://subtlepatterns.subtlepatterns.netdna-cdn.com/patterns/wild_oliva.png);\r\n}\r\n.centered {\r\n  margin:50px auto;\r\n  text-align:center;\r\n}\r\n.button::-moz-focus-inner{\r\n  border: 0;\r\n  padding: 0;\r\n}\r\n.button{\r\n  display: inline-block;\r\n  *display: inline;\r\n  zoom: 1;\r\n  padding: 6px 20px;\r\n  margin: 0;\r\n  cursor: pointer;\r\n  border: 1px solid #bbb;\r\n  overflow: visible;\r\n  font: bold 13px arial, helvetica, sans-serif;\r\n  text-decoration: none;\r\n  white-space: nowrap;\r\n  color: #555;\r\n  \r\n  background-color: #ddd;\r\n  background-image: linear-gradient(to bottom, rgba(255,255,255,1), rgba(255,255,255,0)); /* Changed this from \"top\" to \"to bottom\" */\r\n  transition: background-color .2s ease-out;\r\n  background-clip: padding-box; /* Fix bleeding */\r\n  border-radius: 3px;\r\n  box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;\r\n  text-shadow: 0 1px 0 rgba(255,255,255, .9);\r\n  \r\n  -webkit-touch-callout: none;\r\n  -webkit-user-select: none;\r\n  -moz-user-select: none;\r\n  -ms-user-select: none;\r\n  user-select: none;\r\n}\r\n.button:hover{\r\n  background-color: #eee;\r\n  color: #555;\r\n}\r\n.button:active{\r\n  background: #e9e9e9;\r\n  position: relative;\r\n  top: 1px;\r\n  text-shadow: none;\r\n  box-shadow: 0 1px 1px rgba(0, 0, 0, .3) inset;\r\n}\r\n.button[disabled], .button[disabled]:hover, .button[disabled]:active{\r\n  border-color: #eaeaea;\r\n  background: #fafafa;\r\n  cursor: default;\r\n  position: static;\r\n  color: #999;\r\n  /* Usually, !important should be avoided but here it's really needed :) */\r\n  box-shadow: none !important;\r\n  text-shadow: none !important;\r\n}\r\n/* Smaller buttons styles */\r\n.button.small{\r\n  padding: 4px 12px;\r\n}\r\n/* Larger buttons styles */\r\n.button.large{\r\n  padding: 12px 30px;\r\n  text-transform: uppercase;\r\n}\r\n.button.large:active{\r\n  top: 2px;\r\n}\r\n/* Colored buttons styles */\r\n.button.green, .button.red, .button.blue {\r\n  color: #fff;\r\n  text-shadow: 0 1px 0 rgba(0,0,0,.2);\r\n  background-image: linear-gradient(to bottom, rgba(255,255,255,.3), rgba(255,255,255,0));\r\n}\r\n/* */\r\n.button.green{\r\n  background-color: #57a957;\r\n  border-color: #57a957;\r\n}\r\n.button.green:hover{\r\n  background-color: #62c462;\r\n}\r\n.button.green:active{\r\n  background: #57a957;\r\n}\r\n/* */\r\n.button.red{\r\n  background-color: #ca3535;\r\n  border-color: #c43c35;\r\n}\r\n.button.red:hover{\r\n  background-color: #ee5f5b;\r\n}\r\n.button.red:active{\r\n  background: #c43c35;\r\n}\r\n/* */\r\n.button.blue{\r\n  background-color: #269CE9;\r\n  border-color: #269CE9;\r\n}\r\n.button.blue:hover{\r\n  background-color: #70B9E8;\r\n}\r\n.button.blue:active{\r\n  background: #269CE9;\r\n}\r\n/* */\r\n.green[disabled], .green[disabled]:hover, .green[disabled]:active{\r\n  border-color: #57A957;\r\n  background: #57A957;\r\n  color: #D2FFD2;\r\n}\r\n.red[disabled], .red[disabled]:hover, .red[disabled]:active{\r\n  border-color: #C43C35;\r\n  background: #C43C35;\r\n  color: #FFD3D3;\r\n}\r\n.blue[disabled], .blue[disabled]:hover, .blue[disabled]:active{\r\n  border-color: #269CE9;\r\n  background: #269CE9;\r\n  color: #93D5FF;\r\n}\r\n/* Group buttons */\r\n.button-group,\r\n.button-group li{\r\n  display: inline-block;\r\n  *display: inline;\r\n  zoom: 1;\r\n}\r\n.button-group{\r\n  font-size: 0; /* Inline block elements gap - fix */\r\n  margin: 0;\r\n  padding: 0;\r\n  background: rgba(0, 0, 0, .1);\r\n  border-bottom: 1px solid rgba(0, 0, 0, .1);\r\n  padding: 7px;\r\n  border-radius: 7px;\r\n}\r\n.button-group li{\r\n  margin-right: -1px; /* Overlap each right button border */\r\n}\r\n.button-group .button{\r\n  font-size: 13px; /* Set the font size, different from inherited 0 */\r\n  border-radius: 0;\r\n}\r\n.button-group .button:active{\r\n  box-shadow: 0 0 1px rgba(0, 0, 0, .2) inset, 5px 0 5px -3px rgba(0, 0, 0, .2) inset, -5px 0 5px -3px rgba(0, 0, 0, .2) inset;\r\n}\r\n.button-group li:first-child .button{\r\n  border-radius: 3px 0 0 3px;\r\n}\r\n.button-group li:first-child .button:active{\r\n  box-shadow: 0 0 1px rgba(0, 0, 0, .2) inset, -5px 0 5px -3px rgba(0, 0, 0, .2) inset;\r\n}\r\n.button-group li:last-child .button{\r\n  border-radius: 0 3px 3px 0;\r\n}\r\n.button-group li:last-child .button:active{\r\n  box-shadow: 0 0 1px rgba(0, 0, 0, .2) inset, 5px 0 5px -3px rgba(0, 0, 0, .2) inset;\r\n}"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.html":
/*!*********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.html ***!
  \*********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"centered\">\n        <button class=\"small button\">Button</button>\n        <button class=\"small red button\">Button</button>\n        <button class=\"small green button\">Button</button>\n        <button class=\"small blue button\">Button</button>\n        \n        <br><br>\n        \n        <button class=\"small button\" disabled>Button</button>\n        <button class=\"small red button\" disabled>Button</button>\n        <button class=\"small green button\" disabled>Button</button>\n        <button class=\"small blue button\" disabled>Button</button>\n        \n        <br><br>\n        \n        <ul class=\"button-group\">\n        <li><button class=\"small button\">Button</button></li>\n        <li><button class=\"small button\">Button</button></li>\n        <li><button class=\"small button\">Button</button></li>\n        <li><button class=\"small button\">Button</button></li>\n        </ul>\n        \n        <br><br><br><br>\n        \n        <button class=\"button\">Button</button>\n        <button class=\"red button\">Button</button>\n        <button class=\"green button\">Button</button>\n        <button class=\"blue button\">Button</button>\n        \n        <br><br>\n        \n        <button class=\"button\" disabled>Button</button>\n        <button class=\"red button\" disabled>Button</button>\n        <button class=\"green button\" disabled>Button</button>\n        <button class=\"blue button\" disabled>Button</button>\n        \n        <br><br>\n        \n        <ul class=\"button-group\">\n        <li><button class=\"button\">Button</button></li>\n        <li><button class=\"button\">Button</button></li>\n        <li><button class=\"button\">Button</button></li>\n        <li><button class=\"button\">Button</button></li>\n        </ul>\n        \n        <br><br><br><br>\n        \n        <button class=\"large button\">Button</button>\n        <button class=\"large red button\">Button</button>\n        <button class=\"large green button\">Button</button>\n        <button class=\"large blue button\">Button</button>\n        \n        <br><br>\n        \n        <button class=\"large button\" disabled>Button</button>\n        <button class=\"large red button\" disabled>Button</button>\n        <button class=\"large green button\" disabled>Button</button>\n        <button class=\"large blue button\" disabled>Button</button>\n        \n        <br><br>\n        \n        <ul class=\"button-group\">\n        <li><button class=\"large button\">Button</button></li>\n        <li><button class=\"large button\">Button</button></li>\n        <li><button class=\"large button\">Button</button></li>\n        <li><button class=\"large button\">Button</button></li>\n        </ul>\n          \n          <br><br>\n          \n          <ul class=\"button-group\">\n        <li><button class=\"large red button\">Button</button></li>\n        <li><button class=\"large red button\">Button</button></li>\n        <li><button class=\"large red button\">Button</button></li>\n        <li><button class=\"large red button\">Button</button></li>\n        </ul>\n        </div>\n"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.ts":
/*!*******************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.ts ***!
  \*******************************************************************************************************/
/*! exports provided: IndStockProdComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IndStockProdComponent", function() { return IndStockProdComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm5/index.js");
/* harmony import */ var _stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../stock-services/processed-stock.service */ "./src/app/home/features/stock/stock-services/processed-stock.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var IndStockProdComponent = /** @class */ (function () {
    function IndStockProdComponent(fb, elRef, processedStockService) {
        this.fb = fb;
        this.elRef = elRef;
        this.processedStockService = processedStockService;
        this._amounts = new rxjs__WEBPACK_IMPORTED_MODULE_2__["BehaviorSubject"]([]);
        this.changeProductName = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
    }
    Object.defineProperty(IndStockProdComponent.prototype, "amounts", {
        set: function (value) {
            this._amounts.next(value);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(IndStockProdComponent.prototype, "products", {
        get: function () {
            return this._amounts.getValue();
        },
        enumerable: true,
        configurable: true
    });
    IndStockProdComponent.prototype.ngOnInit = function () {
        var _this = this;
        this._amounts.subscribe(function (amounts) {
            _this.buildAmountForm(amounts);
        });
    };
    IndStockProdComponent.prototype.buildAmountForm = function (amounts) {
        this.amountForm = this.fb.group({
            amounting: this.fb.array(amounts),
        });
    };
    IndStockProdComponent.prototype.submitResult = function () {
        this.processedStockService.submitResult(this.amountForm.controls.amounting.value, this.productName);
    };
    IndStockProdComponent.prototype.addAmount = function () {
        var control = this.amountForm.controls['amounting'];
        control.push(this.initItemRows());
    };
    IndStockProdComponent.prototype.initItemRows = function () {
        return this.fb.control('');
    };
    IndStockProdComponent.prototype.changeProduct = function (name) {
        this.changeProductName.emit(name);
    };
    IndStockProdComponent.prototype.keyboardSetup = function (arrayNumber) {
        this.arrayNumber = arrayNumber;
    };
    IndStockProdComponent.prototype.keyboardClick = function (number) {
        var inputVar = '#inputNames' + this.arrayNumber;
        var val = this.amountForm.controls.amounting.value[this.arrayNumber];
        if (number !== 'minus') {
            this.amountForm.controls.amounting.value[this.arrayNumber] = val + number;
        }
        else {
            console.log('I should be subtrackting right now');
        }
        this.submitResult();
        this.changeProduct(this.productName);
        this.elRef.nativeElement.querySelector(inputVar).focus();
        console.log(this.amountForm.controls.amounting.value[this.arrayNumber], this.productName);
    };
    IndStockProdComponent.prototype.ngOnDestroy = function () {
        this._amounts.unsubscribe();
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", String)
    ], IndStockProdComponent.prototype, "productName", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], IndStockProdComponent.prototype, "amounts", null);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"])(),
        __metadata("design:type", _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"])
    ], IndStockProdComponent.prototype, "changeProductName", void 0);
    IndStockProdComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-ind-stock-prod',
            template: __webpack_require__(/*! ./ind-stock-prod.component.html */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.html"),
            styles: [__webpack_require__(/*! ./ind-stock-prod.component.css */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormBuilder"],
            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"],
            _stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_3__["ProcessedStockService"]])
    ], IndStockProdComponent);
    return IndStockProdComponent;
}());

// "RV1":"3*4,5,20,10*7,10"
//        3*4,5,20,10*7,10
// "RV1":["3*4","5","20","10*7","10"]


/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.css":
/*!**********************************************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.css ***!
  \**********************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.html":
/*!***********************************************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.html ***!
  \***********************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.ts":
/*!*********************************************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.ts ***!
  \*********************************************************************************************************************************/
/*! exports provided: IndStockContainerComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IndStockContainerComponent", function() { return IndStockContainerComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var IndStockContainerComponent = /** @class */ (function () {
    function IndStockContainerComponent() {
    }
    IndStockContainerComponent.prototype.ngOnInit = function () {
    };
    IndStockContainerComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-ind-stock-container',
            template: __webpack_require__(/*! ./ind-stock-container.component.html */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.html"),
            styles: [__webpack_require__(/*! ./ind-stock-container.component.css */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], IndStockContainerComponent);
    return IndStockContainerComponent;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.css":
/*!**********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.css ***!
  \**********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "h3 {\r\n    margin-top: 2px;\r\n}\r\n\r\nh3.inline {\r\n    display: inline;\r\n    padding-left: 10px;\r\n}\r\n\r\nh5.inline {\r\n    display: inline;\r\n    padding-left: 10px;\r\n}\r\n\r\nfieldset h3 {\r\n    margin: 2px;\r\n    color: saddlebrown;\r\n}\r\n\r\n.inputs input {\r\n    width: 80px;\r\n    font-size: 2em;\r\n    margin: 5px;\r\n}\r\n\r\nbutton {\r\n    margin: 5px;\r\n    font-size: 1.2em;\r\n}\r\n\r\n.main {\r\n    margin: 20px;\r\n    padding: 10px;\r\n    background-color: #ffbe7d;\r\n    border-radius: 5px;\r\n    box-shadow: 10px 10px 5px #888;\r\n    }\r\n\r\n.container {\r\n    margin: 3px;\r\n}\r\n\r\n.redButton {\r\n\tbox-shadow:inset 0px 1px 0px 0px #f5978e;\r\n\tbackground:linear-gradient(to bottom, #f24537 5%, #c62d1f 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#f24537', endColorstr='#c62d1f',GradientType=0);\r\n\tbackground-color:#f24537;\r\n\tborder-radius:6px;\r\n\tborder:1px solid #d02718;\r\n\tdisplay:inline-block;\r\n\tcursor:pointer;\r\n\tcolor:#ffffff;\r\n\tfont-family:Arial;\r\n\tfont-size:15px;\r\n\tfont-weight:bold;\r\n\tpadding:6px 6px;\r\n\ttext-decoration:none;\r\n\ttext-shadow:0px 1px 0px #810e05;\r\n}\r\n\r\n.redButton:hover {\r\n\tbackground:linear-gradient(to bottom, #c62d1f 5%, #f24537 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#c62d1f', endColorstr='#f24537',GradientType=0);\r\n\tbackground-color:#c62d1f;\r\n}\r\n\r\n.redButton:active {\r\n\tposition:relative;\r\n\ttop:1px;\r\n}\r\n\r\n.greenButton {\r\n\tbox-shadow:inset 0px 1px 0px 0px #a4e271;\r\n\tbackground:linear-gradient(to bottom, #89c403 5%, #77a809 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#89c403', endColorstr='#77a809',GradientType=0);\r\n\tbackground-color:#89c403;\r\n\tborder-radius:6px;\r\n\tborder:1px solid #74b807;\r\n\tdisplay:inline-block;\r\n\tcursor:pointer;\r\n\tcolor:#ffffff;\r\n\tfont-family:Arial;\r\n\tfont-size:15px;\r\n\tfont-weight:bold;\r\n\tpadding:6px 9px;\r\n\ttext-decoration:none;\r\n\ttext-shadow:0px 1px 0px #528009;\r\n}\r\n\r\n.greenButton:hover {\r\n\tbackground:linear-gradient(to bottom, #77a809 5%, #89c403 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#77a809', endColorstr='#89c403',GradientType=0);\r\n\tbackground-color:#77a809;\r\n}\r\n\r\n.greenButton:active {\r\n\tposition:relative;\r\n\ttop:1px;\r\n}\r\n\r\n.goldButton {\r\n\tbox-shadow:inset 0px 1px 0px 0px #fff6af;\r\n\tbackground:linear-gradient(to bottom, #ffec64 5%, #ffab23 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffec64', endColorstr='#ffab23',GradientType=0);\r\n\tbackground-color:#ffec64;\r\n\tborder-radius:6px;\r\n\tborder:1px solid #ffaa22;\r\n\tdisplay:inline-block;\r\n\tcursor:pointer;\r\n\tcolor:#333333;\r\n\tfont-family:Arial;\r\n\tfont-size:15px;\r\n\tfont-weight:bold;\r\n\tpadding:6px 24px;\r\n\ttext-decoration:none;\r\n\ttext-shadow:0px 1px 0px #ffee66;\r\n}\r\n\r\n.goldButton:hover {\r\n\tbackground:linear-gradient(to bottom, #ffab23 5%, #ffec64 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffab23', endColorstr='#ffec64',GradientType=0);\r\n\tbackground-color:#ffab23;\r\n}\r\n\r\n.goldButton:active {\r\n\tposition:relative;\r\n\ttop:1px;\r\n}\r\n"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.html":
/*!***********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.html ***!
  \***********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div *ngIf='containers' class='main'>\r\n    <form [formGroup]=\"amountForm\" (ngSubmit)='amountFormSubmit()'>\r\n        <h3>Product: {{productName.product}} - {{prodDescription}}</h3>\r\n        <div *ngFor='let con of containers.containers'>\r\n            <fieldset class='container'>\r\n                <h3 class='inline' id='miniH3'>{{con}}</h3>\r\n                <h5 class='inline'>{{prodDescription}}</h5> <br>\r\n                <div formArrayName=\"mainContainer\">\r\n                    <div *ngFor=\"let comp of amountForm.get('mainContainer')['controls']; let i=index\">\r\n                        <span *ngIf='comp.value.container==con'>\r\n                            <div [formGroupName]=\"i\">\r\n                                <div formArrayName=\"amount\">\r\n                                    <span #myInput *ngFor=\"let project of comp.get('amount')['controls']; let j=index\" class=\"inputs\">\r\n                                        <span [formGroupName]=\"j\" >\r\n                                            <input type=\"text\" formControlName=\"amount\" (keyup)='amountFormSubmit()'/>\r\n                                            <span>\r\n                                                <button class='redButton' type=\"button\" (click)=\"deleteProject(comp.controls.amount, j)\">X</button>\r\n                                            </span>\r\n                                        </span>\r\n                                    </span>\r\n                                    <div>\r\n                                        <button class='greenButton' type=\"button\" (click)=\"addNewProject(comp.controls.amount)\">Add</button>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </span>\r\n                    </div>\r\n                </div>\r\n            </fieldset>\r\n        </div>\r\n        <!-- <button class='goldButton' type=\"submit\">Submit Total</button> -->\r\n    </form>\r\n    <!-- <pre>{{amountForm.value | json}}</pre> -->\r\n</div>"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.ts":
/*!*********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.ts ***!
  \*********************************************************************************************************/
/*! exports provided: IndStockProd2Component */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IndStockProd2Component", function() { return IndStockProd2Component; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _stock_services_processed_stock_form_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../stock-services/processed-stock-form.service */ "./src/app/home/features/stock/stock-services/processed-stock-form.service.ts");
/* harmony import */ var _node_modules_angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../../../../../../../node_modules/@angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _stock_services_Stock__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../stock-services/Stock */ "./src/app/home/features/stock/stock-services/Stock.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var IndStockProd2Component = /** @class */ (function () {
    function IndStockProd2Component(processedStockFormService, fb) {
        this.processedStockFormService = processedStockFormService;
        this.fb = fb;
    }
    IndStockProd2Component.prototype.ngOnInit = function () {
        this.buildForm();
    };
    IndStockProd2Component.prototype.buildForm = function () {
        this.amountForm = this.fb.group({
            mainContainer: this.fb.array([])
        });
        this.setCompanies();
    };
    IndStockProd2Component.prototype.setCompanies = function () {
        var _this = this;
        var control = this.amountForm.controls.mainContainer;
        this.productName.mainContainer.forEach(function (x) {
            control.push(_this.fb.group({
                container: x.container,
                amount: _this.setProjects(x)
            }));
        });
    };
    IndStockProd2Component.prototype.setProjects = function (x) {
        var _this = this;
        var arr = new _node_modules_angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormArray"]([]);
        x.amount.forEach(function (y) {
            arr.push(_this.fb.group({
                amount: y
            }));
        });
        return arr;
    };
    IndStockProd2Component.prototype.deleteProject = function (control, index) {
        control.removeAt(index);
        this.processedStockFormService.turnIntoProductUnit(this.productName.product, this.amountForm.value);
    };
    IndStockProd2Component.prototype.addNewProject = function (control) {
        control.push(this.fb.group({
            amount: ['']
        }));
    };
    IndStockProd2Component.prototype.amountFormSubmit = function () {
        // console.log(this.amountForm.value);
        this.processedStockFormService.turnIntoProductUnit(this.productName.product, this.amountForm.value);
    };
    IndStockProd2Component.prototype.ngOnChanges = function (changes) {
        if (changes['productName']) {
            this.buildForm();
            // console.log(this.productName);
            // this.buildAmountForm(this.productName);
        }
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", _stock_services_Stock__WEBPACK_IMPORTED_MODULE_3__["IProcessedStockProducts"])
    ], IndStockProd2Component.prototype, "productName", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object)
    ], IndStockProd2Component.prototype, "containers", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object)
    ], IndStockProd2Component.prototype, "prodDescription", void 0);
    IndStockProd2Component = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-ind-stock-prod2',
            template: __webpack_require__(/*! ./ind-stock-prod2.component.html */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.html"),
            styles: [__webpack_require__(/*! ./ind-stock-prod2.component.css */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.css")]
        }),
        __metadata("design:paramtypes", [_stock_services_processed_stock_form_service__WEBPACK_IMPORTED_MODULE_1__["ProcessedStockFormService"], _node_modules_angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormBuilder"]])
    ], IndStockProd2Component);
    return IndStockProd2Component;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.css":
/*!**********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.css ***!
  \**********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "table {\r\n    font-family: arial, sans-serif;\r\n    /*border-collapse: collapse;*/\r\n    width: 100%;\r\n    font-size: 1.2em;\r\n    border-collapse:separate; \r\n    border-spacing: 0 .8em;\r\n}\r\n\r\ntable h3 {\r\n    margin-top: 0px;\r\n}\r\n\r\ntd, th {\r\n    font-size: .9rem;\r\n    border: 1px solid #dddddd;\r\n    text-align: left;\r\n    padding: 2px;\r\n}\r\n\r\ntr:nth-child(even) {\r\n    background-color: #dddddd;\r\n}\r\n"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.html":
/*!***********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.html ***!
  \***********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<table>\n    <div *ngFor=\"let group of processedGroup\">\n        <div *ngIf=\"group.group == batch\">\n            <h3>{{group.group}}</h3>\n            <tr>\n                <th>Brand</th>\n                <th>Packaging</th>\n                <th>Weight</th>\n                <th>Code</th>\n            </tr>\n            <tr *ngFor=\"let stock of group.stock\">\n                <td>{{stock.brand}}</td>\n                <td>{{stock.packaging}}</td>\n                <td>{{stock.unitweight}}kg</td>\n                <td>\n                    <a class='buttonMenus' (click)=\"changeProduct(stock.productid, stock.description)\">{{stock.productid}}</a>\n                </td>\n            </tr>\n        </div>\n    </div>\n</table>"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.ts":
/*!*********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.ts ***!
  \*********************************************************************************************************/
/*! exports provided: IndStockTableComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IndStockTableComponent", function() { return IndStockTableComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var IndStockTableComponent = /** @class */ (function () {
    function IndStockTableComponent() {
        this.changeProductName = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
    }
    IndStockTableComponent.prototype.ngOnInit = function () {
    };
    IndStockTableComponent.prototype.changeProduct = function (name, desc) {
        var prod = { name: name, description: desc };
        this.changeProductName.emit(prod);
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object)
    ], IndStockTableComponent.prototype, "processedGroup", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object)
    ], IndStockTableComponent.prototype, "batch", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"])(),
        __metadata("design:type", _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"])
    ], IndStockTableComponent.prototype, "changeProductName", void 0);
    IndStockTableComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-ind-stock-table',
            template: __webpack_require__(/*! ./ind-stock-table.component.html */ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.html"),
            styles: [__webpack_require__(/*! ./ind-stock-table.component.css */ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], IndStockTableComponent);
    return IndStockTableComponent;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.css":
/*!****************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.css ***!
  \****************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.html":
/*!*****************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.html ***!
  \*****************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<p>\n  num-keyboard works!\n</p>\n"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.ts":
/*!***************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.ts ***!
  \***************************************************************************************************/
/*! exports provided: NumKeyboardComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "NumKeyboardComponent", function() { return NumKeyboardComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var NumKeyboardComponent = /** @class */ (function () {
    function NumKeyboardComponent() {
    }
    NumKeyboardComponent.prototype.ngOnInit = function () {
    };
    NumKeyboardComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-num-keyboard',
            template: __webpack_require__(/*! ./num-keyboard.component.html */ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.html"),
            styles: [__webpack_require__(/*! ./num-keyboard.component.css */ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], NumKeyboardComponent);
    return NumKeyboardComponent;
}());



/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.css":
/*!********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.css ***!
  \********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".wrapper {\r\n    display: -ms-grid;\r\n    display: grid;\r\n    grid-gap: 10px;\r\n    -ms-grid-columns: (minmax(45%, 0.45fr))[auto-fill];\r\n        grid-template-columns: repeat(auto-fill, minmax(45%, 0.45fr) ) ;\r\n}\r\n\r\n.groups {\r\n    -ms-grid-row-align: start;\r\n        align-self: start;\r\n}\r\n\r\n#finishButton {\r\n    background-color: rgb(211, 106, 112);\r\n    /* float: right; */\r\n}\r\n\r\n#spanning{\r\n    display: -ms-grid;\r\n    display: grid;\r\n    white-space: nowrap;\r\n    -ms-grid-columns: (minmax(150px, 1fr))[auto-fill];\r\n        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));\r\n}\r\n\r\nh3 {\r\n    font-size: 1.3em;\r\n    margin-top: 0px;\r\n}\r\n\r\nh3.inline{\r\n    display: inline;\r\n    padding-left: 10px;\r\n}\r\n\r\n.buttonMenus {\r\n    margin: 5px;\r\n}\r\n\r\n.goldButton {\r\n\tbox-shadow:inset 0px 1px 0px 0px #fff6af;\r\n\tbackground:linear-gradient(to bottom, #ffec64 5%, #ffab23 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffec64', endColorstr='#ffab23',GradientType=0);\r\n\tbackground-color:#ffec64;\r\n\tborder-radius:6px;\r\n\tborder:1px solid #ffaa22;\r\n\tdisplay:inline-block;\r\n\tcursor:pointer;\r\n\tcolor:#333333;\r\n\tfont-family:Arial;\r\n\tfont-size:15px;\r\n\tfont-weight:bold;\r\n\tpadding:6px 24px;\r\n\ttext-decoration:none;\r\n    text-shadow:0px 1px 0px #ffee66;\r\n    margin-top: 10px;\r\n    margin-bottom: 10px;\r\n    margin-right: 5px;\r\n}\r\n\r\n.goldButton:hover {\r\n\tbackground:linear-gradient(to bottom, #ffab23 5%, #ffec64 100%);\r\n\tfilter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffab23', endColorstr='#ffec64',GradientType=0);\r\n\tbackground-color:#ffab23;\r\n}\r\n\r\n.goldButton:active {\r\n\tposition:relative;\r\n\ttop:1px;\r\n}"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.html":
/*!*********************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.html ***!
  \*********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<button class='goldButton' (click)=\"submitToDataBase()\" >FINISH AND SAVE</button>\n<button class='goldButton' (click)=\"clearAllProducts()\" >Clear All Products</button>\n<h3 class='inline'>{{stocktime}}</h3>\n<div *ngIf=\"processedGroup && processedStockMain\">\n    <app-ind-stock-prod2 *ngIf='productName && productContainerOptions' \n        [productName]='productNameWithContainer' \n        [containers]='productContainerOptions'\n        [prodDescription]='productDescription'>\n    </app-ind-stock-prod2>\n    <div class='wrapper'>\n        <div class='groups' id='spanning'>\n            <h3>Batch Groups</h3><br>\n            <a class='buttonMenus' *ngFor=\"let group of processedGroup\" (click)=\"BatchGroup(group.group)\">{{group.group}}</a>\n        </div>\n        <app-ind-stock-table *ngIf=\"processedGroup\" \n            [processedGroup]=\"processedGroup\" \n            [batch]=\"batch\" \n            (changeProductName)=\"changeProduct($event)\">\n        </app-ind-stock-table>\n    </div>\n</div>"

/***/ }),

/***/ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.ts":
/*!*******************************************************************************************************!*\
  !*** ./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.ts ***!
  \*******************************************************************************************************/
/*! exports provided: StockProductsComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StockProductsComponent", function() { return StockProductsComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm5/index.js");
/* harmony import */ var _stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../../stock-services/processed-stock.service */ "./src/app/home/features/stock/stock-services/processed-stock.service.ts");
/* harmony import */ var _stock_services_stock_api_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../stock-services/stock-api.service */ "./src/app/home/features/stock/stock-services/stock-api.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var StockProductsComponent = /** @class */ (function () {
    function StockProductsComponent(processedStockService, stockAPIService) {
        this.processedStockService = processedStockService;
        this.stockAPIService = stockAPIService;
        this._productNames = new rxjs__WEBPACK_IMPORTED_MODULE_1__["BehaviorSubject"]([]);
        this.productName = 'Select a product';
        this.productNameWithContainer = {};
        this.processedStock = {};
        this.amounts = [];
    }
    Object.defineProperty(StockProductsComponent.prototype, "productNames", {
        get: function () {
            return this._productNames.getValue();
        },
        set: function (value) {
            this._productNames.next(value);
        },
        enumerable: true,
        configurable: true
    });
    StockProductsComponent.prototype.ngOnInit = function () {
        var _this = this;
        // this can probably all be done in parent component and just the group inserted here without any change detection
        this._productNames.subscribe(function (x) {
            _this.processedGroup = _this.processedStockService.groupByCategory(_this.productNames);
        });
    };
    StockProductsComponent.prototype.BatchGroup = function (batch) {
        this.batch = batch;
        console.log(this.batch);
        this.productContainerOptions = undefined;
    };
    StockProductsComponent.prototype.changeProduct = function (product) {
        this.processedStockMain = JSON.parse(localStorage.getItem('stock'));
        // this.processedStockMain = [];
        for (var i = 0; i < this.processedStockMain.length; ++i) {
            if (this.processedStockMain[i].product === product.name) {
                this.productNameWithContainer = this.processedStockMain[i];
                this.productDescription = product.description;
                this.getContainers(product.name);
                return;
            }
        }
        console.log('There was no stock');
        this.productNameWithContainer = {};
    };
    StockProductsComponent.prototype.getContainers = function (productName) {
        var holder = { name: '', containers: [] };
        for (var i = 0; i < this.processedStockMain.length; ++i) {
            if (this.processedStockMain[i].product === productName) {
                holder.name = this.processedStockMain[i].product;
                for (var j = 0; j < this.processedStockMain[i].mainContainer.length; ++j) {
                    holder.containers.push(this.processedStockMain[i].mainContainer[j].container);
                }
                this.productContainerOptions = holder;
            }
        }
    };
    StockProductsComponent.prototype.submitToDataBase = function () {
        this.processedStockService.insertProcStockIntoDB(this.stocktime);
    };
    StockProductsComponent.prototype.clearAllProducts = function () {
        this.processedStockService.clearAllProducts(this.stocktime);
    };
    StockProductsComponent.prototype.ngOnDestroy = function () {
        this._productNames.unsubscribe();
    };
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Array)
    ], StockProductsComponent.prototype, "processedStockMain", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])(),
        __metadata("design:type", Object)
    ], StockProductsComponent.prototype, "stocktime", void 0);
    __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"])() // This can just load with *ngIF cause it only comes in once (Just normal list of productnames)
        ,
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], StockProductsComponent.prototype, "productNames", null);
    StockProductsComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-stock-products',
            template: __webpack_require__(/*! ./stock-products.component.html */ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.html"),
            styles: [__webpack_require__(/*! ./stock-products.component.css */ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.css")]
        }),
        __metadata("design:paramtypes", [_stock_services_processed_stock_service__WEBPACK_IMPORTED_MODULE_2__["ProcessedStockService"],
            _stock_services_stock_api_service__WEBPACK_IMPORTED_MODULE_3__["StockAPIService"]])
    ], StockProductsComponent);
    return StockProductsComponent;
}());

// TODO: Make Colored LED's that shows if there is a connection, and also if there is data that needs to be saved.


/***/ }),

/***/ "./src/app/home/features/stock/stock-services/Stock.ts":
/*!*************************************************************!*\
  !*** ./src/app/home/features/stock/stock-services/Stock.ts ***!
  \*************************************************************/
/*! exports provided: IProductDetails, IProductGroup, IProcessedStockProducts, IProcessedStockContainer, IRawProcessedStock, IProductContainers, IContainerGroups */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IProductDetails", function() { return IProductDetails; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IProductGroup", function() { return IProductGroup; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IProcessedStockProducts", function() { return IProcessedStockProducts; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IProcessedStockContainer", function() { return IProcessedStockContainer; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IRawProcessedStock", function() { return IRawProcessedStock; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IProductContainers", function() { return IProductContainers; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IContainerGroups", function() { return IContainerGroups; });
var IProductDetails = /** @class */ (function () {
    function IProductDetails(brand, packaging, weight, code, batchGroup, description) {
        this.brand = brand;
        this.packaging = packaging;
        this.unitweight = weight;
        this.productid = code;
        this.batchgroup = batchGroup;
        this.description = description;
    }
    return IProductDetails;
}());

var IProductGroup = /** @class */ (function () {
    function IProductGroup() {
    }
    return IProductGroup;
}());

// -------------------------------------------------------------------
var IProcessedStockProducts = /** @class */ (function () {
    function IProcessedStockProducts() {
    }
    return IProcessedStockProducts;
}());

var IProcessedStockContainer = /** @class */ (function () {
    function IProcessedStockContainer() {
    }
    return IProcessedStockContainer;
}());

// -------------------------------------------------------------------
var IRawProcessedStock = /** @class */ (function () {
    function IRawProcessedStock() {
    }
    return IRawProcessedStock;
}());

var IProductContainers = /** @class */ (function () {
    function IProductContainers() {
    }
    return IProductContainers;
}());

var IContainerGroups = /** @class */ (function () {
    function IContainerGroups() {
    }
    return IContainerGroups;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stock-services/my-input.directive.ts":
/*!**************************************************************************!*\
  !*** ./src/app/home/features/stock/stock-services/my-input.directive.ts ***!
  \**************************************************************************/
/*! exports provided: MyInputDirective */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MyInputDirective", function() { return MyInputDirective; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var MyInputDirective = /** @class */ (function () {
    function MyInputDirective(elem) {
        this.elem = elem;
        this.firstTime = true;
    }
    MyInputDirective.prototype.ngAfterViewInit = function () {
        if (this.firstTime) {
            this.elem.nativeElement.focus();
            this.firstTime = false;
        }
    };
    MyInputDirective = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Directive"])({
            selector: 'input[type=text]'
        }),
        __metadata("design:paramtypes", [_angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"]])
    ], MyInputDirective);
    return MyInputDirective;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stock-services/processed-stock-form.service.ts":
/*!************************************************************************************!*\
  !*** ./src/app/home/features/stock/stock-services/processed-stock-form.service.ts ***!
  \************************************************************************************/
/*! exports provided: ProcessedStockFormService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ProcessedStockFormService", function() { return ProcessedStockFormService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var ProcessedStockFormService = /** @class */ (function () {
    function ProcessedStockFormService(fb) {
        this.fb = fb;
    }
    ProcessedStockFormService.prototype.turnIntoProductUnit = function (productName, containerAmounts) {
        // console.log('I am hit');
        var productUnit = { product: productName, mainContainer: [] };
        for (var a = 0; a < containerAmounts.mainContainer.length; ++a) {
            var amount = [];
            for (var b = 0; b < containerAmounts.mainContainer[a].amount.length; ++b) {
                if (containerAmounts.mainContainer[a].amount[b].amount !== '') {
                    amount.push(containerAmounts.mainContainer[a].amount[b].amount);
                }
            }
            var container = { container: containerAmounts.mainContainer[a].container, amount: amount };
            productUnit.mainContainer.push(container);
            // console.log('-------- ', containerAmounts.mainContainer[a]);
        }
        // console.log('-------- ', containerAmounts.mainContainer);
        this.checkToSeeIfProductThere(productUnit);
    };
    ProcessedStockFormService.prototype.checkToSeeIfProductThere = function (productName) {
        var stock = JSON.parse(localStorage.getItem('stock'));
        for (var prodnum = 0; prodnum < stock.length; ++prodnum) {
            if (stock[prodnum].product === productName.product) {
                stock[prodnum].mainContainer = productName.mainContainer;
                localStorage.removeItem('stock');
                localStorage.setItem('stock', JSON.stringify(stock));
                return;
            }
        }
        console.log('------ STOCK DOES NOT EXIST !!!!! ------ ');
    };
    ProcessedStockFormService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormBuilder"]])
    ], ProcessedStockFormService);
    return ProcessedStockFormService;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stock-services/processed-stock.service.ts":
/*!*******************************************************************************!*\
  !*** ./src/app/home/features/stock/stock-services/processed-stock.service.ts ***!
  \*******************************************************************************/
/*! exports provided: ProcessedStockService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ProcessedStockService", function() { return ProcessedStockService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _stock_api_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./stock-api.service */ "./src/app/home/features/stock/stock-services/stock-api.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _node_modules_rxjs__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../../../../node_modules/rxjs */ "./node_modules/rxjs/_esm5/index.js");
/* harmony import */ var _core_dialog_box_dialog_box_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../../core/dialog-box/dialog-box.service */ "./src/app/home/core/dialog-box/dialog-box.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};





var ProcessedStockService = /** @class */ (function () {
    function ProcessedStockService(stockAPI, router, dialogBoxService) {
        this.stockAPI = stockAPI;
        this.router = router;
        this.dialogBoxService = dialogBoxService;
        this.personStream = new _node_modules_rxjs__WEBPACK_IMPORTED_MODULE_3__["ReplaySubject"]();
    }
    ProcessedStockService.prototype.insertProcStockIntoDB = function (stocktime) {
        var databaseArray = this.getStockReadyForDatabase(stocktime);
        this.deleteOldStock(stocktime);
        this.insertStockIntoDB(databaseArray);
    };
    ProcessedStockService.prototype.getStockReadyForDatabase = function (stocktime) {
        var finalArray = [];
        var stockArray = JSON.parse(localStorage.getItem('stock'));
        for (var array = 0; array < stockArray.length; ++array) {
            if (stockArray[array].mainContainer.length > 0) {
                for (var mainCon = 0; mainCon < stockArray[array].mainContainer.length; ++mainCon) {
                    if (stockArray[array].mainContainer[mainCon].amount.length > 0) {
                        for (var amt = 0; amt < stockArray[array].mainContainer[mainCon].amount.length; ++amt) {
                            var name_1 = stockArray[array].product;
                            var amount = stockArray[array].mainContainer[mainCon].amount[amt];
                            var container = stockArray[array].mainContainer[mainCon].container;
                            var indProduct = { prodName: name_1, amount: amount, container: container, time: stocktime };
                            finalArray.push(indProduct);
                        }
                    }
                }
            }
        }
        return finalArray;
    };
    ProcessedStockService.prototype.deleteOldStock = function (stocktime) {
        var _this = this;
        this.stockAPI.deleteAllTimeProcessedStock(stocktime).subscribe(function (x) {
            if (!x) {
                console.log('Orders deleted', x);
            }
            else {
                console.log('Orders NOT deleted', x);
                _this.dialogBoxService.openConfirmationDialog();
            }
        });
    };
    ProcessedStockService.prototype.insertStockIntoDB = function (databaseArray) {
        var _this = this;
        this.stockAPI.enterAllProcessedProductsIntoDB(databaseArray).subscribe(function (x) {
            console.log('Number of orders:', databaseArray.length, ', Number of orders inserted:', x.length);
            if (databaseArray.length === x.length) {
                _this.router.navigate(['user/user-nav/']);
            }
            else {
                _this.dialogBoxService.openConfirmationDialog();
            }
        });
    };
    ProcessedStockService.prototype.groupByCategory = function (products) {
        if (!products) {
            return;
        } // This helps also to avoid an "undefined" error
        var categories = new Set(products.map(function (x) { return x.batchgroup; }).sort());
        var result = Array.from(categories).map(function (x) { return ({
            group: x,
            stock: products.filter(function (stocks) { return stocks.batchgroup === x; })
        }); });
        return result;
    };
    ProcessedStockService.prototype.submitResult = function (amount, productName) {
        amount = this.removeZeros(amount);
        var key = productName;
        if (localStorage['stock']) {
            var JSObject = JSON.parse(localStorage.getItem('stock'));
            var b = amount.toString();
            JSObject[key] = b;
            localStorage.setItem('stock', JSON.stringify(JSObject));
        }
        //    this.changeProduct('Select next product');
    };
    ProcessedStockService.prototype.removeZeros = function (array) {
        for (var i = array.length - 1; i >= 0; i--) {
            if (array[i] === '0' || array[i] === '') {
                array.splice(i, 1);
            }
        }
        return array;
    };
    ProcessedStockService.prototype.calculateTotal = function (amountArray) {
        var val;
        var total = 0;
        for (var _i = 0, amountArray_1 = amountArray; _i < amountArray_1.length; _i++) {
            val = amountArray_1[_i];
            console.log(Function('"use strict"; return (' + val + ')')());
            total = total + Function('"use strict"; return (' + val + ')')();
        }
        return total;
    };
    ProcessedStockService.prototype.getTestdata = function () {
        var _this = this;
        this.stockAPI.getProducts().subscribe(function (response) {
            _this.personStream.next(response);
        });
    };
    ProcessedStockService.prototype.clearAllProducts = function (stocktime) {
        var _this = this;
        this.stockAPI.deleteAllTimeProcessedStock(stocktime)
            .subscribe(function (x) {
            console.log(x);
            _this.router.navigate(['user/user-nav/']);
            _this.dialogBoxService.openStockClearedDialog();
        });
    };
    ProcessedStockService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_stock_api_service__WEBPACK_IMPORTED_MODULE_1__["StockAPIService"],
            _angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"],
            _core_dialog_box_dialog_box_service__WEBPACK_IMPORTED_MODULE_4__["DialogBoxService"]])
    ], ProcessedStockService);
    return ProcessedStockService;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stock-services/stock-api.service.ts":
/*!*************************************************************************!*\
  !*** ./src/app/home/features/stock/stock-services/stock-api.service.ts ***!
  \*************************************************************************/
/*! exports provided: StockAPIService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StockAPIService", function() { return StockAPIService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _core_urls_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../core/urls.service */ "./src/app/home/core/urls.service.ts");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var StockAPIService = /** @class */ (function () {
    function StockAPIService(http, urlService) {
        this.http = http;
        this.urlService = urlService;
        // http://192.168.45.2:8000/api/products/containers
        this.productsUrl = this.urlService.rootUrl + 'api/products/';
    }
    StockAPIService.prototype.getProducts = function () {
        return this.http.get(this.productsUrl);
    };
    StockAPIService.prototype.getTimedStock = function (time) {
        var timeUrl = this.productsUrl + time + '/';
        console.log(timeUrl);
        return this.http.get(timeUrl);
    };
    StockAPIService.prototype.getProductContainers = function () {
        var timeUrl = this.productsUrl + 'containers/';
        console.log(timeUrl);
        return this.http.get(timeUrl);
    };
    StockAPIService.prototype.deleteAllTimeProcessedStock = function (time) {
        var timeUrl = this.productsUrl + 'delete/' + time;
        return this.http.delete(timeUrl);
    };
    StockAPIService.prototype.enterAllProcessedProductsIntoDB = function (finalArray) {
        return this.http.post(this.productsUrl + 'input/', finalArray);
    };
    StockAPIService.prototype.getHardcodedStock = function () {
        var procStock = [];
        var SV1 = { product: 'SV1', mainContainer: [
                { container: 'Box', amount: ['3', '4', '7 * 9', '5'] },
                { container: 'Bulk Bags', amount: ['1', '2'] },
                { container: 'Crate', amount: ['6', '7', '8 * 9'] }
            ] };
        var RV1 = { product: 'RV1', mainContainer: [
                { container: 'Box', amount: ['3'] },
                { container: 'Pasturised', amount: ['1', '2', '3 * 4', '5'] },
                { container: 'Bulk Bags', amount: ['6', '9*9'] }
            ] };
        var SG2 = { product: 'SG2', mainContainer: [
                { container: 'Box', amount: ['3', '4', '7 * 9', '22', '9*9', '6*6'] },
                { container: 'Bulk Bags', amount: ['1', '2', '3 * 4', '5'] },
                { container: 'Crate', amount: ['6', '7', '1'] },
                { container: 'Lugs', amount: ['5*5', '2*5'] }
            ] };
        procStock.push(SV1, RV1, SG2);
        return procStock;
    };
    StockAPIService.prototype.getHardcodedProductContainers = function () {
        var prodContainers = [
            { name: 'SV1', containers: ['Box', 'Bulk Bags', 'Crate'] },
            { name: 'RV1', containers: ['Box', 'Pasturised', 'Crate', 'Bulk Bags'] },
            { name: 'SG2', containers: ['Box', 'Bulk Bags', 'Crate', 'Lugs'] }
        ];
        return prodContainers;
    };
    StockAPIService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_2__["HttpClient"], _core_urls_service__WEBPACK_IMPORTED_MODULE_1__["UrlsService"]])
    ], StockAPIService);
    return StockAPIService;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stocks-routing.module.ts":
/*!**************************************************************!*\
  !*** ./src/app/home/features/stock/stocks-routing.module.ts ***!
  \**************************************************************/
/*! exports provided: StocksRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StocksRoutingModule", function() { return StocksRoutingModule; });
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _processed_get_products_get_products_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./processed/get-products/get-products.component */ "./src/app/home/features/stock/processed/get-products/get-products.component.ts");
/* harmony import */ var _shared_user_entry_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../shared/user-entry.component */ "./src/app/home/shared/user-entry.component.ts");
/* harmony import */ var _shared_under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../shared/under-construction/under-construction.component */ "./src/app/home/shared/under-construction/under-construction.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};





var stockRoutes = [
    {
        path: 'user',
        component: _shared_user_entry_component__WEBPACK_IMPORTED_MODULE_3__["UserEntryComponent"],
        children: [
            {
                path: 'stock-taking',
                component: _shared_under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_4__["UnderConstructionComponent"]
            },
            {
                path: 'processed/:time',
                component: _processed_get_products_get_products_component__WEBPACK_IMPORTED_MODULE_2__["GetProductsComponent"]
            },
        ]
    }
];
var StocksRoutingModule = /** @class */ (function () {
    function StocksRoutingModule() {
    }
    StocksRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(stockRoutes)],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
        })
    ], StocksRoutingModule);
    return StocksRoutingModule;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stocks.component.css":
/*!**********************************************************!*\
  !*** ./src/app/home/features/stock/stocks.component.css ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".leftDiv {\r\n    float:left;\r\n    width: 20%;\r\n}\r\n\r\n.buttonMenus{\r\n    margin: 10px;\r\n    font-size: 1.5em;\r\n}\r\n\r\nh3 {\r\n    margin: 0px;\r\n}\r\n\r\nh1 {\r\n    color: rgb(172, 22, 47);\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    font-size: 200%;\r\n  }\r\n\r\na {\r\n    cursor: pointer;\r\n    cursor: hand;\r\n  }\r\n\r\n.center-screen {\r\n    flex-direction: column;\r\n    justify-content: center;\r\n    align-items: center;\r\n    text-align: center;\r\n  }\r\n\r\nnav a {\r\n    padding: 5px 10px;\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    text-decoration: none;\r\n    margin-right: 5px;\r\n    margin-top: 20px;\r\n    display: inline-block;\r\n    background-color: #eee;\r\n    border-radius: 4px;\r\n  }\r\n\r\nnav a:visited, a:link {\r\n    color: #607D8B;\r\n  }\r\n\r\nnav a:hover {\r\n    color: rgb(172, 22, 47);\r\n    background-color: #CFD8DC;\r\n  }\r\n\r\nnav a.active {\r\n    color: rgb(172, 22, 47);\r\n  }"

/***/ }),

/***/ "./src/app/home/features/stock/stocks.component.html":
/*!***********************************************************!*\
  !*** ./src/app/home/features/stock/stocks.component.html ***!
  \***********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<h2>Stocktaking</h2>\n<br>\n<div>\n    <div class='leftDiv'>\n        <h3>Processed</h3>\n        <a class='buttonMenus' routerLink=\"../processed/06:00\" routerLinkActive=\"active\">06:00</a>\n        <br>\n        <a class='buttonMenus' routerLink=\"../processed/12:00\" routerLinkActive=\"active\">12:00</a>\n        <br>\n        <a class='buttonMenus' routerLink=\"../processed/18:00\" routerLinkActive=\"active\">18:00</a>\n    </div>\n    <div>\n        <h3>Raw Material</h3>\n        <a class='buttonMenus' routerLink=\"../processed\" routerLinkActive=\"active\">Daily</a>\n        <br>\n        <a class='buttonMenus' routerLink=\"../processed\" routerLinkActive=\"active\">End of week</a>\n    </div>\n</div>\n<router-outlet></router-outlet> "

/***/ }),

/***/ "./src/app/home/features/stock/stocks.component.ts":
/*!*********************************************************!*\
  !*** ./src/app/home/features/stock/stocks.component.ts ***!
  \*********************************************************/
/*! exports provided: StocksComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StocksComponent", function() { return StocksComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var StocksComponent = /** @class */ (function () {
    function StocksComponent() {
    }
    StocksComponent.prototype.ngOnInit = function () {
    };
    StocksComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-stocks',
            template: __webpack_require__(/*! ./stocks.component.html */ "./src/app/home/features/stock/stocks.component.html"),
            styles: [__webpack_require__(/*! ./stocks.component.css */ "./src/app/home/features/stock/stocks.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], StocksComponent);
    return StocksComponent;
}());



/***/ }),

/***/ "./src/app/home/features/stock/stocks.module.ts":
/*!******************************************************!*\
  !*** ./src/app/home/features/stock/stocks.module.ts ***!
  \******************************************************/
/*! exports provided: StocksModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StocksModule", function() { return StocksModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _stocks_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./stocks.component */ "./src/app/home/features/stock/stocks.component.ts");
/* harmony import */ var _stocks_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./stocks-routing.module */ "./src/app/home/features/stock/stocks-routing.module.ts");
/* harmony import */ var _processed_get_products_get_products_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./processed/get-products/get-products.component */ "./src/app/home/features/stock/processed/get-products/get-products.component.ts");
/* harmony import */ var _processed_get_products_stock_products_stock_products_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./processed/get-products/stock-products/stock-products.component */ "./src/app/home/features/stock/processed/get-products/stock-products/stock-products.component.ts");
/* harmony import */ var _processed_get_products_ind_stock_prod_ind_stock_prod_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./processed/get-products/ind-stock-prod/ind-stock-prod.component */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod/ind-stock-prod.component.ts");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _processed_get_products_ind_stock_table_ind_stock_table_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./processed/get-products/ind-stock-table/ind-stock-table.component */ "./src/app/home/features/stock/processed/get-products/ind-stock-table/ind-stock-table.component.ts");
/* harmony import */ var _processed_get_products_num_keyboard_num_keyboard_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./processed/get-products/num-keyboard/num-keyboard.component */ "./src/app/home/features/stock/processed/get-products/num-keyboard/num-keyboard.component.ts");
/* harmony import */ var _processed_get_products_ind_stock_prod2_ind_stock_prod2_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./processed/get-products/ind-stock-prod2/ind-stock-prod2.component */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-prod2.component.ts");
/* harmony import */ var _processed_get_products_ind_stock_prod2_ind_stock_container_ind_stock_container_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component */ "./src/app/home/features/stock/processed/get-products/ind-stock-prod2/ind-stock-container/ind-stock-container.component.ts");
/* harmony import */ var _stock_services_my_input_directive__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./stock-services/my-input.directive */ "./src/app/home/features/stock/stock-services/my-input.directive.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};













var StocksModule = /** @class */ (function () {
    function StocksModule() {
    }
    StocksModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                _stocks_routing_module__WEBPACK_IMPORTED_MODULE_3__["StocksRoutingModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"]
            ],
            declarations: [
                _stocks_component__WEBPACK_IMPORTED_MODULE_2__["StocksComponent"],
                _processed_get_products_get_products_component__WEBPACK_IMPORTED_MODULE_4__["GetProductsComponent"],
                _processed_get_products_stock_products_stock_products_component__WEBPACK_IMPORTED_MODULE_5__["StockProductsComponent"],
                _processed_get_products_ind_stock_prod_ind_stock_prod_component__WEBPACK_IMPORTED_MODULE_6__["IndStockProdComponent"],
                _processed_get_products_ind_stock_table_ind_stock_table_component__WEBPACK_IMPORTED_MODULE_8__["IndStockTableComponent"],
                _processed_get_products_num_keyboard_num_keyboard_component__WEBPACK_IMPORTED_MODULE_9__["NumKeyboardComponent"],
                _processed_get_products_ind_stock_prod2_ind_stock_prod2_component__WEBPACK_IMPORTED_MODULE_10__["IndStockProd2Component"],
                _processed_get_products_ind_stock_prod2_ind_stock_container_ind_stock_container_component__WEBPACK_IMPORTED_MODULE_11__["IndStockContainerComponent"],
                _stock_services_my_input_directive__WEBPACK_IMPORTED_MODULE_12__["MyInputDirective"],
            ],
            providers: []
        })
    ], StocksModule);
    return StocksModule;
}());



/***/ }),

/***/ "./src/app/home/home.component.css":
/*!*****************************************!*\
  !*** ./src/app/home/home.component.css ***!
  \*****************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\nimg {\r\n  max-width: 100%;\r\n  height: auto;\r\n  width: auto\\9;\r\n}\r\n\r\n.mainImg{\r\n  background-color: #ffdbb7;\r\n  -ms-grid-column: 2;\r\n  -ms-grid-column-span: 2;\r\n  grid-column: 2/4;\r\n  -ms-grid-row: 2;\r\n  -ms-grid-row-span: 2;\r\n  grid-row: 2/4;\r\n}\r\n\r\n#packaging {\r\n  -ms-grid-column: 3;\r\n      grid-column-start: 3;\r\n  -ms-grid-row: 3;\r\n      grid-row-start: 3;\r\n}\r\n\r\n/*\r\n\r\n.wrapper {\r\n  display: grid;\r\n  max-width: auto;\r\n  max-height: 800px;\r\n  grid-template-columns: 50vw?????????????????????? 300px 1fr 300px 175px 175px 50px;\r\n  grid-template-rows: 50px 50px 150px 150px 150px 150px 150px 150px 150px 150px 1fr 1fr;\r\n}\r\n\r\n.mainImg{\r\n  background-color: #ffdbb7;\r\n  grid-column: 2/7;\r\n  grid-row: 2/7;\r\n}\r\n\r\napp-website-nav{\r\n  background-color: rgb(172, 22, 47);\r\n  grid-column: 6/8;\r\n  grid-row: 3;\r\n  max-height: 150px;\r\n  padding: 5px;\r\n}\r\n\r\n#packaging {\r\n  grid-column: 6/8;\r\n  grid-row: 5;\r\n}\r\n\r\n#mrLogo {\r\n  grid-column-start: 3;\r\n  grid-row-start: 1;\r\n}\r\n\r\n#samples {\r\n  grid-column: 6/8;\r\n  grid-row: 7;\r\n}\r\n\r\nimg {\r\n  max-width: 100%;\r\n  height: auto;\r\n  width: auto\\9;\r\n}\r\n\r\nh1 {\r\n    z-index: 1;\r\n    background-color: #ffdbb7;\r\n    grid-column-start: 2;\r\n    grid-row-start: 1;\r\n    justify-content: center;\r\n    color: rgb(172, 22, 47);\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    font-size: 200%;\r\n  }\r\n\r\n  a {\r\n    cursor: pointer;\r\n    cursor: hand;\r\n  }\r\n  \r\n  .center-screen {\r\n    flex-direction: column;\r\n    justify-content: center;\r\n    align-items: center;\r\n    text-align: center;\r\n  }\r\n\r\n  nav a {\r\n    padding: 5px 10px;\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    text-decoration: none;\r\n    margin-right: 5px;\r\n    margin-top: 20px;\r\n    display: inline-block;\r\n    background-color: #eee;\r\n    border-radius: 4px;\r\n  }\r\n\r\n\r\n  \r\n  nav a:visited, a:link {\r\n    color: #607D8B;\r\n  }\r\n  nav a:hover {\r\n    color: rgb(172, 22, 47);\r\n    background-color: #CFD8DC;\r\n  }\r\n  nav a.active {\r\n    color: rgb(172, 22, 47);\r\n  }\r\n\r\n  */"

/***/ }),

/***/ "./src/app/home/home.component.html":
/*!******************************************!*\
  !*** ./src/app/home/home.component.html ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-auth-alert></app-auth-alert>\r\n<router-outlet></router-outlet>"

/***/ }),

/***/ "./src/app/home/home.component.ts":
/*!****************************************!*\
  !*** ./src/app/home/home.component.ts ***!
  \****************************************/
/*! exports provided: HomeComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HomeComponent", function() { return HomeComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var HomeComponent = /** @class */ (function () {
    function HomeComponent() {
    }
    HomeComponent.prototype.ngOnInit = function () {
    };
    HomeComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-home',
            template: __webpack_require__(/*! ./home.component.html */ "./src/app/home/home.component.html"),
            styles: [__webpack_require__(/*! ./home.component.css */ "./src/app/home/home.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], HomeComponent);
    return HomeComponent;
}());



/***/ }),

/***/ "./src/app/home/shared/under-construction/under-construction.component.css":
/*!*********************************************************************************!*\
  !*** ./src/app/home/shared/under-construction/under-construction.component.css ***!
  \*********************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "div.horizontal {\r\n    display: flex;\r\n    justify-content: center;\r\n    margin-top: 50px;\r\n}\r\n\r\ndiv.vertical {\r\n    display: flex;\r\n    flex-direction: column;\r\n    justify-content: center;\r\n}\r\n\r\nimg {\r\n    box-shadow: 5px 5px 10px #888;\r\n    }"

/***/ }),

/***/ "./src/app/home/shared/under-construction/under-construction.component.html":
/*!**********************************************************************************!*\
  !*** ./src/app/home/shared/under-construction/under-construction.component.html ***!
  \**********************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"horizontal div1\">\n    <div class=\"vertical\">\n        <img src=\"assets/images/uConstruction.jpg\">\n    </div>\n</div>"

/***/ }),

/***/ "./src/app/home/shared/under-construction/under-construction.component.ts":
/*!********************************************************************************!*\
  !*** ./src/app/home/shared/under-construction/under-construction.component.ts ***!
  \********************************************************************************/
/*! exports provided: UnderConstructionComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UnderConstructionComponent", function() { return UnderConstructionComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var UnderConstructionComponent = /** @class */ (function () {
    function UnderConstructionComponent() {
    }
    UnderConstructionComponent.prototype.ngOnInit = function () {
    };
    UnderConstructionComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-under-construction',
            template: __webpack_require__(/*! ./under-construction.component.html */ "./src/app/home/shared/under-construction/under-construction.component.html"),
            styles: [__webpack_require__(/*! ./under-construction.component.css */ "./src/app/home/shared/under-construction/under-construction.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], UnderConstructionComponent);
    return UnderConstructionComponent;
}());



/***/ }),

/***/ "./src/app/home/shared/user-entry-routing.module.ts":
/*!**********************************************************!*\
  !*** ./src/app/home/shared/user-entry-routing.module.ts ***!
  \**********************************************************/
/*! exports provided: UserEntryRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserEntryRoutingModule", function() { return UserEntryRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _features_stock_stocks_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../features/stock/stocks.component */ "./src/app/home/features/stock/stocks.component.ts");
/* harmony import */ var _user_entry_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./user-entry.component */ "./src/app/home/shared/user-entry.component.ts");
/* harmony import */ var _user_nav_user_nav_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./user-nav/user-nav.component */ "./src/app/home/shared/user-nav/user-nav.component.ts");
/* harmony import */ var _under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./under-construction/under-construction.component */ "./src/app/home/shared/under-construction/under-construction.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};






var userEntryRoutes = [
    {
        path: 'user',
        component: _user_entry_component__WEBPACK_IMPORTED_MODULE_3__["UserEntryComponent"],
        children: [
            {
                path: 'user',
                component: _user_nav_user_nav_component__WEBPACK_IMPORTED_MODULE_4__["UserNavComponent"],
            },
            {
                path: 'user-nav',
                component: _user_nav_user_nav_component__WEBPACK_IMPORTED_MODULE_4__["UserNavComponent"],
            },
            {
                path: 'stocks',
                component: _features_stock_stocks_component__WEBPACK_IMPORTED_MODULE_2__["StocksComponent"],
            },
            {
                path: 'L-shape',
                component: _under_construction_under_construction_component__WEBPACK_IMPORTED_MODULE_5__["UnderConstructionComponent"],
            },
        ],
    },
];
var UserEntryRoutingModule = /** @class */ (function () {
    function UserEntryRoutingModule() {
    }
    UserEntryRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forChild(userEntryRoutes)],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]]
        })
    ], UserEntryRoutingModule);
    return UserEntryRoutingModule;
}());



/***/ }),

/***/ "./src/app/home/shared/user-entry.component.css":
/*!******************************************************!*\
  !*** ./src/app/home/shared/user-entry.component.css ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".buttonMenus {\r\n    justify-content: right;\r\n    align-items: right;\r\n    text-align: right;\r\n  }"

/***/ }),

/***/ "./src/app/home/shared/user-entry.component.html":
/*!*******************************************************!*\
  !*** ./src/app/home/shared/user-entry.component.html ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<a class='buttonMenus' routerLink=\"user-nav\" routerLinkActive=\"active\">Main</a>\n<a class='buttonMenus' routerLink=\"../login\" routerLinkActive=\"active\">Log Out</a>\n<br>\n<router-outlet></router-outlet>\n"

/***/ }),

/***/ "./src/app/home/shared/user-entry.component.ts":
/*!*****************************************************!*\
  !*** ./src/app/home/shared/user-entry.component.ts ***!
  \*****************************************************/
/*! exports provided: UserEntryComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserEntryComponent", function() { return UserEntryComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var UserEntryComponent = /** @class */ (function () {
    function UserEntryComponent() {
    }
    UserEntryComponent.prototype.ngOnInit = function () {
    };
    UserEntryComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-user-entry',
            template: __webpack_require__(/*! ./user-entry.component.html */ "./src/app/home/shared/user-entry.component.html"),
            styles: [__webpack_require__(/*! ./user-entry.component.css */ "./src/app/home/shared/user-entry.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], UserEntryComponent);
    return UserEntryComponent;
}());



/***/ }),

/***/ "./src/app/home/shared/user-entry.module.ts":
/*!**************************************************!*\
  !*** ./src/app/home/shared/user-entry.module.ts ***!
  \**************************************************/
/*! exports provided: UserEntryModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserEntryModule", function() { return UserEntryModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _user_entry_routing_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./user-entry-routing.module */ "./src/app/home/shared/user-entry-routing.module.ts");
/* harmony import */ var _features_stock_stocks_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../features/stock/stocks.module */ "./src/app/home/features/stock/stocks.module.ts");
/* harmony import */ var _user_entry_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./user-entry.component */ "./src/app/home/shared/user-entry.component.ts");
/* harmony import */ var _user_nav_user_nav_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./user-nav/user-nav.component */ "./src/app/home/shared/user-nav/user-nav.component.ts");
/* harmony import */ var _features_factory_factory_module__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../features/factory/factory.module */ "./src/app/home/features/factory/factory.module.ts");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ngx-permissions */ "./node_modules/ngx-permissions/ngx-permissions.umd.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(ngx_permissions__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _features_admin_register_user_register_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../features/admin/register-user/register.component */ "./src/app/home/features/admin/register-user/register.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};









var UserEntryModule = /** @class */ (function () {
    function UserEntryModule() {
    }
    UserEntryModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                _user_entry_routing_module__WEBPACK_IMPORTED_MODULE_2__["UserEntryRoutingModule"],
                ngx_permissions__WEBPACK_IMPORTED_MODULE_7__["NgxPermissionsModule"].forChild(),
                _features_stock_stocks_module__WEBPACK_IMPORTED_MODULE_3__["StocksModule"],
                _features_factory_factory_module__WEBPACK_IMPORTED_MODULE_6__["FactoryModule"]
            ],
            declarations: [
                _user_entry_component__WEBPACK_IMPORTED_MODULE_4__["UserEntryComponent"],
                _user_nav_user_nav_component__WEBPACK_IMPORTED_MODULE_5__["UserNavComponent"],
                _features_admin_register_user_register_component__WEBPACK_IMPORTED_MODULE_8__["RegisterComponent"],
            ]
        })
    ], UserEntryModule);
    return UserEntryModule;
}());



/***/ }),

/***/ "./src/app/home/shared/user-nav/user-nav.component.css":
/*!*************************************************************!*\
  !*** ./src/app/home/shared/user-nav/user-nav.component.css ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "h1 {\r\n    color: rgb(172, 22, 47);\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    font-size: 200%;\r\n  }\r\n\r\n  a {\r\n    cursor: pointer;\r\n    cursor: hand;\r\n  }\r\n\r\n  .center-screen {\r\n    flex-direction: column;\r\n    justify-content: center;\r\n    align-items: center;\r\n    text-align: center;\r\n  }\r\n\r\n  nav a {\r\n    padding: 5px 10px;\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    text-decoration: none;\r\n    margin-right: 5px;\r\n    margin-top: 20px;\r\n    display: inline-block;\r\n    background-color: #eee;\r\n    border-radius: 4px;\r\n  }\r\n\r\n  nav a:visited, a:link {\r\n    color: #607D8B;\r\n  }\r\n\r\n  nav a:hover {\r\n    color: rgb(172, 22, 47);\r\n    background-color: #CFD8DC;\r\n  }\r\n\r\n  nav a.active {\r\n    color: rgb(172, 22, 47);\r\n  }"

/***/ }),

/***/ "./src/app/home/shared/user-nav/user-nav.component.html":
/*!**************************************************************!*\
  !*** ./src/app/home/shared/user-nav/user-nav.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"center-screen\">\n    <nav>\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor', 'Lshape-leader', 'shift-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Stock</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../factory\" routerLinkActive=\"active\">Factory</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Production</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['shift-supervisor','factory-supervisor','Lshape-leader']\">\n            <a class='buttonMenus' routerLink=\"../L-shape\" routerLinkActive=\"active\">L-Shape</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['shift-supervisor','factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Storage</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['shift-supervisor','factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Receiving</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Factory Office</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Workshop</a>\n        </ng-template>\n\n        <ng-template [ngxPermissionsOnly]=\"['factory-supervisor']\">\n            <a class='buttonMenus' routerLink=\"../stocks\" routerLinkActive=\"active\">Food safety</a>\n        </ng-template>\n    </nav>\n</div>"

/***/ }),

/***/ "./src/app/home/shared/user-nav/user-nav.component.ts":
/*!************************************************************!*\
  !*** ./src/app/home/shared/user-nav/user-nav.component.ts ***!
  \************************************************************/
/*! exports provided: UserNavComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserNavComponent", function() { return UserNavComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _user_nav_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./user-nav.service */ "./src/app/home/shared/user-nav/user-nav.service.ts");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ngx-permissions */ "./node_modules/ngx-permissions/ngx-permissions.umd.js");
/* harmony import */ var ngx_permissions__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(ngx_permissions__WEBPACK_IMPORTED_MODULE_2__);
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var UserNavComponent = /** @class */ (function () {
    function UserNavComponent(permissionsService, _userNav) {
        this.permissionsService = permissionsService;
        this._userNav = _userNav;
        this.permissions = [];
    }
    UserNavComponent.prototype.ngOnInit = function () {
        var _this = this;
        this._userNav.getPermissions().subscribe(function (groups) {
            for (var _i = 0, _a = Object.keys(groups.groups); _i < _a.length; _i++) {
                var key = _a[_i];
                _this.permissions.push(groups.groups[key].name);
            }
            _this.permissionsService.loadPermissions(_this.permissions);
            console.log(_this.permissions);
        });
    };
    UserNavComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-user-nav',
            template: __webpack_require__(/*! ./user-nav.component.html */ "./src/app/home/shared/user-nav/user-nav.component.html"),
            styles: [__webpack_require__(/*! ./user-nav.component.css */ "./src/app/home/shared/user-nav/user-nav.component.css")]
        }),
        __metadata("design:paramtypes", [ngx_permissions__WEBPACK_IMPORTED_MODULE_2__["NgxPermissionsService"], _user_nav_service__WEBPACK_IMPORTED_MODULE_1__["UserNavService"]])
    ], UserNavComponent);
    return UserNavComponent;
}());



/***/ }),

/***/ "./src/app/home/shared/user-nav/user-nav.service.ts":
/*!**********************************************************!*\
  !*** ./src/app/home/shared/user-nav/user-nav.service.ts ***!
  \**********************************************************/
/*! exports provided: UserNavService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserNavService", function() { return UserNavService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _core_urls_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../core/urls.service */ "./src/app/home/core/urls.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var UserNavService = /** @class */ (function () {
    function UserNavService(http, _urlService) {
        this.http = http;
        this._urlService = _urlService;
        this.permissions = this._urlService.rootUrl + 'api/test/';
    }
    UserNavService.prototype.getPermissions = function () {
        return this.http.get(this.permissions);
    };
    UserNavService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"], _core_urls_service__WEBPACK_IMPORTED_MODULE_2__["UrlsService"]])
    ], UserNavService);
    return UserNavService;
}());



/***/ }),

/***/ "./src/app/home/website/about/about.component.css":
/*!********************************************************!*\
  !*** ./src/app/home/website/about/about.component.css ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/website/about/about.component.html":
/*!*********************************************************!*\
  !*** ./src/app/home/website/about/about.component.html ***!
  \*********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "I am about"

/***/ }),

/***/ "./src/app/home/website/about/about.component.ts":
/*!*******************************************************!*\
  !*** ./src/app/home/website/about/about.component.ts ***!
  \*******************************************************/
/*! exports provided: AboutComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AboutComponent", function() { return AboutComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var AboutComponent = /** @class */ (function () {
    function AboutComponent() {
    }
    AboutComponent.prototype.ngOnInit = function () {
    };
    AboutComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-about',
            template: __webpack_require__(/*! ./about.component.html */ "./src/app/home/website/about/about.component.html"),
            styles: [__webpack_require__(/*! ./about.component.css */ "./src/app/home/website/about/about.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], AboutComponent);
    return AboutComponent;
}());



/***/ }),

/***/ "./src/app/home/website/contact/contact.component.css":
/*!************************************************************!*\
  !*** ./src/app/home/website/contact/contact.component.css ***!
  \************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/website/contact/contact.component.html":
/*!*************************************************************!*\
  !*** ./src/app/home/website/contact/contact.component.html ***!
  \*************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<p>\n  contact works!\n</p>\n"

/***/ }),

/***/ "./src/app/home/website/contact/contact.component.ts":
/*!***********************************************************!*\
  !*** ./src/app/home/website/contact/contact.component.ts ***!
  \***********************************************************/
/*! exports provided: ContactComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ContactComponent", function() { return ContactComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var ContactComponent = /** @class */ (function () {
    function ContactComponent() {
    }
    ContactComponent.prototype.ngOnInit = function () {
    };
    ContactComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-contact',
            template: __webpack_require__(/*! ./contact.component.html */ "./src/app/home/website/contact/contact.component.html"),
            styles: [__webpack_require__(/*! ./contact.component.css */ "./src/app/home/website/contact/contact.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], ContactComponent);
    return ContactComponent;
}());



/***/ }),

/***/ "./src/app/home/website/website-home/website-home.component.css":
/*!**********************************************************************!*\
  !*** ./src/app/home/website/website-home/website-home.component.css ***!
  \**********************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\nimg {\r\n    max-width: 100%;\r\n    height: auto;\r\n    width: auto\\9;\r\n  }\r\n  \r\n  .mainImg{\r\n    background-color: #ffdbb7;\r\n    -ms-grid-column: 2;\r\n    -ms-grid-column-span: 2;\r\n    grid-column: 2/4;\r\n    -ms-grid-row: 2;\r\n    -ms-grid-row-span: 2;\r\n    grid-row: 2/4;\r\n  }\r\n  \r\n  #packaging {\r\n    -ms-grid-column: 3;\r\n        grid-column-start: 3;\r\n    -ms-grid-row: 3;\r\n        grid-row-start: 3;\r\n  }"

/***/ }),

/***/ "./src/app/home/website/website-home/website-home.component.html":
/*!***********************************************************************!*\
  !*** ./src/app/home/website/website-home/website-home.component.html ***!
  \***********************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<img class=\"mainImg\" alt=\"Meatrite Logo\" src=\"assets/images/mainMix.jpg\">"

/***/ }),

/***/ "./src/app/home/website/website-home/website-home.component.ts":
/*!*********************************************************************!*\
  !*** ./src/app/home/website/website-home/website-home.component.ts ***!
  \*********************************************************************/
/*! exports provided: WebsiteHomeComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteHomeComponent", function() { return WebsiteHomeComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var WebsiteHomeComponent = /** @class */ (function () {
    function WebsiteHomeComponent() {
    }
    WebsiteHomeComponent.prototype.ngOnInit = function () {
    };
    WebsiteHomeComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-website-home',
            template: __webpack_require__(/*! ./website-home.component.html */ "./src/app/home/website/website-home/website-home.component.html"),
            styles: [__webpack_require__(/*! ./website-home.component.css */ "./src/app/home/website/website-home/website-home.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], WebsiteHomeComponent);
    return WebsiteHomeComponent;
}());



/***/ }),

/***/ "./src/app/home/website/website-nav/website-nav.component.css":
/*!********************************************************************!*\
  !*** ./src/app/home/website/website-nav/website-nav.component.css ***!
  \********************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "h1 {\r\n    color: rgb(172, 22, 47);\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    font-size: 200%;\r\n  }\r\n\r\n  a {\r\n    cursor: pointer;\r\n    cursor: hand;\r\n  }\r\n\r\n  .center-screen {\r\n    flex-direction: column;\r\n    justify-content: center;\r\n    align-items: center;\r\n    text-align: center;\r\n  }\r\n\r\n  nav a {\r\n    padding: 5px 10px;\r\n    font-family: Arial, Helvetica, sans-serif;\r\n    text-decoration: none;\r\n    margin-right: 5px;\r\n    margin-top: 20px;\r\n    display: inline-block;\r\n    background-color: #eee;\r\n    border-radius: 4px;\r\n  }\r\n\r\n  nav a:visited, a:link {\r\n    color: #607D8B;\r\n  }\r\n\r\n  nav a:hover {\r\n    color: rgb(172, 22, 47);\r\n    background-color: #CFD8DC;\r\n  }\r\n\r\n  nav a.active {\r\n    color: rgb(172, 22, 47);\r\n  }"

/***/ }),

/***/ "./src/app/home/website/website-nav/website-nav.component.html":
/*!*********************************************************************!*\
  !*** ./src/app/home/website/website-nav/website-nav.component.html ***!
  \*********************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"center-screen\">\n  <nav>\n    <a routerLink=\"/home\" routerLinkActive=\"active\">Home</a>\n    <a routerLink=\"/about\" routerLinkActive=\"active\">About</a>\n    <a routerLink=\"/contact\" routerLinkActive=\"active\">Contacts</a>\n    <a routerLink=\"/login\" routerLinkActive=\"active\">Login</a>\n    <!-- <a [routerLink]=\"[{outlets: {'websiteNav': ['about']}} ]\">About</a>\n    <a [routerLink]=\"[{outlets: {'websiteNav': ['contact']}} ]\">Contacts</a>\n    <a [routerLink]=\"[{outlets: {'websiteNav': ['login']}} ]\">Login</a> -->\n  </nav>\n</div>\n\n"

/***/ }),

/***/ "./src/app/home/website/website-nav/website-nav.component.ts":
/*!*******************************************************************!*\
  !*** ./src/app/home/website/website-nav/website-nav.component.ts ***!
  \*******************************************************************/
/*! exports provided: WebsiteNavComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteNavComponent", function() { return WebsiteNavComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var WebsiteNavComponent = /** @class */ (function () {
    function WebsiteNavComponent() {
    }
    WebsiteNavComponent.prototype.ngOnInit = function () {
    };
    WebsiteNavComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-website-nav',
            template: __webpack_require__(/*! ./website-nav.component.html */ "./src/app/home/website/website-nav/website-nav.component.html"),
            styles: [__webpack_require__(/*! ./website-nav.component.css */ "./src/app/home/website/website-nav/website-nav.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], WebsiteNavComponent);
    return WebsiteNavComponent;
}());



/***/ }),

/***/ "./src/app/home/website/website-routing.module.ts":
/*!********************************************************!*\
  !*** ./src/app/home/website/website-routing.module.ts ***!
  \********************************************************/
/*! exports provided: WebsiteRoutingModule, WebsiteRoutingComponents */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteRoutingModule", function() { return WebsiteRoutingModule; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteRoutingComponents", function() { return WebsiteRoutingComponents; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _about_about_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./about/about.component */ "./src/app/home/website/about/about.component.ts");
/* harmony import */ var _contact_contact_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./contact/contact.component */ "./src/app/home/website/contact/contact.component.ts");
/* harmony import */ var _features_admin_login_login_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../features/admin/login/login.component */ "./src/app/home/features/admin/login/login.component.ts");
/* harmony import */ var _website_home_website_home_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./website-home/website-home.component */ "./src/app/home/website/website-home/website-home.component.ts");
/* harmony import */ var _website_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./website.component */ "./src/app/home/website/website.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};







var websiteRoutes = [
    {
        path: '',
        component: _website_component__WEBPACK_IMPORTED_MODULE_6__["WebsiteComponent"],
        children: [
            {
                path: '',
                component: _website_home_website_home_component__WEBPACK_IMPORTED_MODULE_5__["WebsiteHomeComponent"],
            },
            {
                path: 'home',
                component: _website_home_website_home_component__WEBPACK_IMPORTED_MODULE_5__["WebsiteHomeComponent"],
            },
            {
                path: 'about',
                component: _about_about_component__WEBPACK_IMPORTED_MODULE_2__["AboutComponent"],
            },
            {
                path: 'contact',
                component: _contact_contact_component__WEBPACK_IMPORTED_MODULE_3__["ContactComponent"],
            },
            {
                path: 'login',
                component: _features_admin_login_login_component__WEBPACK_IMPORTED_MODULE_4__["LoginComponent"],
            }
        ]
    },
];
var WebsiteRoutingModule = /** @class */ (function () {
    function WebsiteRoutingModule() {
    }
    WebsiteRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forChild(websiteRoutes)
            ],
            exports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]
            ],
            providers: []
        })
    ], WebsiteRoutingModule);
    return WebsiteRoutingModule;
}());

var WebsiteRoutingComponents = [_website_home_website_home_component__WEBPACK_IMPORTED_MODULE_5__["WebsiteHomeComponent"], _about_about_component__WEBPACK_IMPORTED_MODULE_2__["AboutComponent"], _contact_contact_component__WEBPACK_IMPORTED_MODULE_3__["ContactComponent"], _features_admin_login_login_component__WEBPACK_IMPORTED_MODULE_4__["LoginComponent"]];


/***/ }),

/***/ "./src/app/home/website/website.component.css":
/*!****************************************************!*\
  !*** ./src/app/home/website/website.component.css ***!
  \****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/home/website/website.component.html":
/*!*****************************************************!*\
  !*** ./src/app/home/website/website.component.html ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class='wrapper'>\n    <app-website-nav></app-website-nav>\n</div>\n\n<router-outlet></router-outlet>"

/***/ }),

/***/ "./src/app/home/website/website.component.ts":
/*!***************************************************!*\
  !*** ./src/app/home/website/website.component.ts ***!
  \***************************************************/
/*! exports provided: WebsiteComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteComponent", function() { return WebsiteComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var WebsiteComponent = /** @class */ (function () {
    function WebsiteComponent() {
    }
    WebsiteComponent.prototype.ngOnInit = function () {
    };
    WebsiteComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-website',
            template: __webpack_require__(/*! ./website.component.html */ "./src/app/home/website/website.component.html"),
            styles: [__webpack_require__(/*! ./website.component.css */ "./src/app/home/website/website.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], WebsiteComponent);
    return WebsiteComponent;
}());



/***/ }),

/***/ "./src/app/home/website/website.module.ts":
/*!************************************************!*\
  !*** ./src/app/home/website/website.module.ts ***!
  \************************************************/
/*! exports provided: WebsiteModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WebsiteModule", function() { return WebsiteModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _website_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./website-routing.module */ "./src/app/home/website/website-routing.module.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var WebsiteModule = /** @class */ (function () {
    function WebsiteModule() {
    }
    WebsiteModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            declarations: [
                _website_routing_module__WEBPACK_IMPORTED_MODULE_3__["WebsiteRoutingComponents"],
            ],
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                _website_routing_module__WEBPACK_IMPORTED_MODULE_3__["WebsiteRoutingModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormsModule"]
            ]
        })
    ], WebsiteModule);
    return WebsiteModule;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build ---prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false
};
/*
 * In development mode, to ignore zone related error stack frames such as
 * `zone.run`, `zoneDelegate.invokeTask` for easier debugging, you can
 * import the following file, but please comment it out in production mode
 * because it will have performance impact when throw error
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.log(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\Users\MRProgrammeringPC\Dropbox\Programming\Angular\meatriteFrontEnd\src\main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map