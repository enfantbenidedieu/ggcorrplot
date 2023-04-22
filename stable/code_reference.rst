
Code Reference
==============

.. _hwggcorrplot:

ggcorrplot
----------

.. note::
    ggcorrplot(x,method = "square",type = "full",ggtheme = pn.theme_minimal(),title = None,show_legend = True,legend_title = "Corr",show_diag = None,colors = ["blue","white","red"],outline_color = "gray",hc_order = False,hc_method = "complete",lab = False,lab_col = "black",lab_size = 11,p_mat = None,sig_level=0.05,insig = "pch",pch = 4,pch_col = "black",pch_cex = 5,tl_cex = 12,tl_col = "black",tl_srt = 45,digits = 2)

A graphical display of a correlation matrix using ``plotnine``.
  
* **Parameters**:
   * **x** (DataFrame) : DataFrame containing multiple variables and observations. Each column represents a variable, and each row a single observation of all those variables.
   * **method** (str) : the visualization method of correlation matrix to be used. Allowed values are ``square`` (default), ``circle``.
   * **type** (str) : ``full`` (default), ``lower`` or ``upper`` display.
   * **ggthme** *()* : plotnine function. Default value is ``theme_minimal``. Allowed values are the official plotnine themes including ``theme_gray``, ``theme_bw``, ``theme_minimal``, ``theme_classic``, ``theme_void``.
   * **title** (str) : title of the graph
   * **show_legend** (bool) : if ``True`` the legend is displayed.
   * **legend_title** (str) : legend title. lower triangular, upper triangular or full matrix.
   * **show_diag** (None|bool) : Whether display the correlation coefficients on the principal diagonal. If ``None``, the default is to show diagonal correlation for ``type=full`` and to remove it when the type is one of ``upper`` or ``lower``.
   * **colors** (list) : a list of 3 colors for low, mid and high correlation values.
   * **outline_color** (str) : the outline color of squared or circle. Default value is ``gray``.
   * **hc_order** (bool) : if ``True``, correlation matrix will be hc_ordered using https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html function.
   * **hc_method** (str) : the linkage method to be used in https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html function.
   * **lab** (bool) : if ``True``, add correlation coefficient on the plot.
   * **lab_col** (str) :  color to be used for the correlation coefficient labels, used when ``lab=True``.
   * **lab_size** (int) : size to be used for correlation coefficient labels, used when ``lab=True``.
   * **p_mat** (DataFrame) : DataFrame of p-value. If ``None``, arguments ``sig_level``, ``insig``, ``pch```, ``pch_col``, ``pch_cex``is invalid.
   * **sig_level** (float) :significant level, if the p-value in p_mat is bigger that sig_level, then the corresponding correlation coefficient is regarded as insignificant.
   * **insig** (str) : specialized insignificant correlation coefficients,  ``pch`` (default), ``blank``. If ``blank``, wipe away the corresponding glyphs; if ``pch``, add string (see ``pch`` for details) on corresponding glyphs.
   * **pch** (int) : add string on the glyphs of insignificant correlation coefficients (only valid when insig is ``pch``). Default value is 4.
   * **pch_col** (str) : the color of pch (only valid when insig is ``pch``).
   * **pch_cex** (int) : the cex (size) of pch (only valid when insig is ``pch``).
   * **tl_cex** (int) : the size of text label (variable names).
   * **tl_col** (str) : the color of text label (variable names).
   * **tl_srt** (int) : the integer rotation of text label (variable names).
   * **digits** (int) : Decides the number of decimal digits to be displayed (Default : ``2``).

.. _hwgetmelt:

get_melt
--------

.. note::
    get_melt(x)

Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

* **Parameters**:
    * **x** (DataFrame) : DataFrame to melt. 
* **Returns** : Unpivoted DataFrame.

.. _hwhccormatorder:

hc_cormat_order
---------------

.. note::
    hc_cormat_order(cormat, method='complete')

Performs hierarchical clustering on a distance or similarity structure.

* **Parameters**:
    * **cormat** (`DataFrame <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html/>`) : correlation matrix
    * **method** (`str <https://docs.python.org/3/library/stdtypes.html#str/>`) : the linkage algorithm to use. See the https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
* **Returns** : dictionary of 6 elements : order of variables, height, method, merge, numbers of observations and the initial dataframe.


.. _hwmatcharg:

match_arg
---------

.. note::
    match_arg(x, lst)

Argument verification using partial matching.

* **Parameters**:
    * **x** (str) : a string arguments.
    * **lst** (`list <https://docs.python.org/3/library/stdtypes.html#list/>`) : a list of candidate values.
* **Return"** : The unabbreviated version of the exact or unique partial match if there is one

.. _hwnopanel:

no_panel
--------

.. note::
    no_panel()

Customize the non - data componennts of your plots. 

.. _hwremovediag:

remove_diag
-----------

.. note::
    remove_diag(cormat)

Fill the main diagonal of the correlation matrix with NA.

* **Parameters** :
    * **cormat** (DataFrame) : correlation matrix.
* **Return** : This function modifies the input array in-place 
  
.. _hwgetuppertri:

get_upper_tri
-------------

.. note::
    get_upper_tri(cormat,show_diag=False)

Get upper triangle of the correlation matrix.

* **Parameters** :
    * **cormat** (DataFrame) : correlation matrix
    * **show_diag** ([bool](https://docs.python.org/3/library/functions.html#bool)) : logical. If ``True``, displays the correlation coefficients.
* **Returns** : Upper triangle of a correlation matrix.

.. _hwgetlowertri:

get_lower_tri
-------------

.. note::
    get_lower_tri(cormat,show_diag=False)

Get lower triangle of the correlation matrix.

* **Parameters**:
    * **cormat** (DataFrame) : correlation matrix
    * **show_diag** (bool) : boolean. If ``True``, displays the correlation coefficients.
* **Returns** : Lower triangle of a correlation matrix.

.. _hwcorpmat:

cor_pmat
--------

.. note::
    cor_pmat(x,**kwargs)

Compute a correlation matrix p-values.

* **Parameters** :
    * **x** ([DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)) : DataFrame containing multiple variables and observations. Each column represents a variable, and each row a single observation of all those variables.
    * ``**kwargs`` : other arguments to be passed to the function  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html.


* **Returns** : DataFrame containing the p-values of correlations.
